from fastapi import FastAPI, APIRouter,Depends,UploadFile,File,status
import os
import aiofiles
from fastapi.responses import JSONResponse
from models import ResponseSignal
from helpers.config import get_settings,Settings
from controllers import DataController,ProjectController,ProcessController
from .schemas.data import ProcessRequest
import logging

logger = logging.getLogger('uvicorn.error')
base_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"],
)

@base_router.post("/upload/{project_id}")
async def upload_data(project_id: str,file:UploadFile,app_settings:Settings = Depends(get_settings)):
    datacontroller = DataController()
    is_valid,result_signal = datacontroller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(status_code= status.HTTP_400_BAD_REQUEST,
               content={
                   'signal':is_valid,
                }
               )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path,file_id = datacontroller.generate_unique_filepath(
        orig_filename= file.filename,
        project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return JSONResponse(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
               content={
                   'signal':ResponseSignal.FILE_UPLOADED_FAILED.value,
                }
               )

    return JSONResponse(
               content={
                   'signal':ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value,
                   "file_id":file_id
                }
               )
@base_router.post('/process/{project_id}')
async def process_endpoint(project_id:str,process_request:ProcessRequest):
    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    
    process_controller = ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )
    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_PROCESSING_FAILED.value
            }
        )
    return file_chunks

        
from enum import Enum

class ResponseSignal(Enum):
    
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_UPLOADED_FAILED = "File upload failed"
    FILE_PROCESSING_FAILED = "File processing failed"
    FILE_PROCESSED_SUCCESSFULLY = "File processed successfully"
    NO_FILES_ERROR = "Not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    PROJECT_NOT_FOUND_ERROR = "project_not_found_error"
    INSERT_INTO_VECTORDB_ERROR = 'insert_into_vector_error'
    INSERT_INTO_VECTORDB_SUCCESS = 'insert_into_vector_success'
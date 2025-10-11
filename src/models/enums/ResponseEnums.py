from enum import Enum

class ResponseSignal(Enum):
    
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_UPLOADED_FAILED = "File upload failed"
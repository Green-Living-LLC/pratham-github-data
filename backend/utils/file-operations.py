import os
from fastapi import UploadFile

async def save_upload_file(upload_file: UploadFile, destination: str) -> str:
    file_path = os.path.join(destination, upload_file.filename)
    with open(file_path, "wb") as buffer:
        content = await upload_file.read()
        buffer.write(content)
    return file_path

def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)

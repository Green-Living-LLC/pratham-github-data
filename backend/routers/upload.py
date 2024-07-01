from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uuid
import datetime
import os
from config import UPLOAD_DIR

router = APIRouter()

@router.post("/api/v1/upload")
async def upload_pdf(file: UploadFile = File(...), time_duration: int = 24):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")
        
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        file_size = os.path.getsize(file_path)
        upload_timestamp = datetime.datetime.now()
        deletion_date_time = upload_timestamp + datetime.timedelta(hours=time_duration)
        
        return JSONResponse(content={
            "file_id": file_id,
            "size": file_size,
            "upload_timestamp": upload_timestamp.isoformat(),
            "deletion_date_time": deletion_date_time.isoformat()
        }, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during file processing: {str(e)}")

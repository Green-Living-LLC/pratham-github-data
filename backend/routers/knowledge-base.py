from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uuid
import datetime
import os
from config import KNOWLEDGE_BASE_DIR

router = APIRouter()

@router.post("/api/v1/knowledge-base")
async def upload_knowledge_base(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(KNOWLEDGE_BASE_DIR, f"{file_id}.pdf")
        
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        return JSONResponse(content={
            "file_id": file_id,
            "filename": file.filename,
            "upload_timestamp": datetime.datetime.now().isoformat()
        }, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during file processing: {str(e)}")

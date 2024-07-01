from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
import asyncio
from config import UPLOAD_DIR, TASKS

router = APIRouter()

async def process_pdf(file_id: str):
    # Simulating PDF processing
    await asyncio.sleep(10)  # Simulate a long-running task
    TASKS[file_id]["status"] = "completed"
    TASKS[file_id]["progress"] = 100

@router.post("/api/v1/process")
async def process_pdf_api(file_id: str, background_tasks: BackgroundTasks):
    if not os.path.exists(os.path.join(UPLOAD_DIR, f"{file_id}.pdf")):
        raise HTTPException(status_code=404, detail="File not found")
    
    task_id = str(uuid.uuid4())
    TASKS[task_id] = {"status": "processing", "progress": 0}
    
    background_tasks.add_task(process_pdf, task_id)
    
    return JSONResponse(content={"task_id": task_id}, status_code=200)

@router.get("/api/v1/process/{task_id}")
async def get_process_status(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return JSONResponse(content=TASKS[task_id], status_code=200)

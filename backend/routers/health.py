from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/v1/healthcheck")
async def health_check():
    try:
        # Perform any necessary health checks here
        return JSONResponse(content={"status": "OK"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")

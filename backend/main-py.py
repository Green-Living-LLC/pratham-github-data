from fastapi import FastAPI
from routers import upload, process, health, knowledge_base, query
import uvicorn

app = FastAPI()

app.include_router(upload.router)
app.include_router(process.router)
app.include_router(health.router)
app.include_router(knowledge_base.router)
app.include_router(query.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

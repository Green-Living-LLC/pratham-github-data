import os

UPLOAD_DIR = "uploads"
KNOWLEDGE_BASE_DIR = "knowledge_base"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)

# Simulating task storage
TASKS = {}

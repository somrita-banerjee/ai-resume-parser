import os
import shutil
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_file(upload_file):
    file_path = UPLOAD_DIR / upload_file.filename
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path
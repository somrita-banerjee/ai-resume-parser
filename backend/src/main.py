from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.file_handler import save_file
from utils.extractor import extract_text
from utils.ai_parser import parse_resume

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    file_path = save_file(file)
    raw_text = extract_text(file_path)
    parsed_data = parse_resume(raw_text)
    return {"parsed": parsed_data}
from fastapi import FastAPI, File, UploadFile
from typing import List
from io import StringIO

app = FastAPI()

@app.post("/extract_skills")
async def extract_skills(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    skills = ["Python", "Machine Learning", "Data Analysis"]

    return {"skills": skills}

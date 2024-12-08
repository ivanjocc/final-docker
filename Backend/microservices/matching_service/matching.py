from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CV(BaseModel):
    name: str
    skills: list

class JobOffer(BaseModel):
    title: str
    description: str
    skills_required: list

@app.post("/match")
async def match(cv: CV, offer: JobOffer):
    # Simulación de matching entre CV y oferta
    score = len(set(cv.skills) & set(offer.skills_required)) / len(offer.skills_required)
    return {"cv_name": cv.name, "job_offer": offer.title, "match_score": score}

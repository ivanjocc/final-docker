from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter()

@router.get("/{cv_id}/matches")
def match_jobs(cv_id: int, db: Session = Depends(database.get_db)):
    cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if not cv:
        return {"error": "CV not found"}
    
    matched_jobs = db.query(models.JobOffer).filter(
        models.JobOffer.required_skills.contains(cv.skills)
    ).all()
    return {"matches": matched_jobs}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/")
def create_job(job: schemas.JobOfferCreate, db: Session = Depends(database.get_db)):
    new_job = models.JobOffer(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return {"message": "Job offer created successfully", "job": new_job}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/")
def create_cv(cv: schemas.CVCreate, db: Session = Depends(database.get_db)):
    new_cv = models.CV(**cv.dict())
    db.add(new_cv)
    db.commit()
    db.refresh(new_cv)
    return {"message": "CV created successfully", "cv": new_cv}

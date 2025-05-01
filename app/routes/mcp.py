from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recommended-itinerary")
def recommend_itinerary(nights: int, db: Session = Depends(get_db)):
    itineraries = db.query(models.Itinerary).filter(models.Itinerary.nights == nights).all()
    if not itineraries:
        raise HTTPException(status_code=404, detail="No itinerary found for that duration")
    return itineraries

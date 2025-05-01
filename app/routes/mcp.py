from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(tags=["Itinerary"])


def get_db():
    """Dependency function to get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/recommended-itinerary", summary="Get Recommended Itinerary", response_description="List of recommended itineraries")
def recommend_itinerary(nights: int, db: Session = Depends(get_db)):
    """
    Fetch a recommended itinerary based on the number of nights.

    Args:
        nights (int): Number of nights for the travel plan.

    Returns:
        A list of itineraries that match the number of nights.
    """
    itineraries = db.query(models.Itinerary).filter(models.Itinerary.nights == nights).all()

    if not itineraries:
        raise HTTPException(status_code=404, detail="No itinerary found for the given number of nights.")

    return itineraries

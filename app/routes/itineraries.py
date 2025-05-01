from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create an itinerary
@router.post("/itineraries/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db, itinerary)

# Get all itineraries
@router.get("/itineraries/", response_model=list[schemas.Itinerary])
def list_itineraries(db: Session = Depends(get_db)):
    return crud.get_itineraries(db)

# Get itinerary by id
@router.get("/itineraries/{id}", response_model=schemas.Itinerary)
def get_itinerary(id: int, db: Session = Depends(get_db)):
    itinerary = crud.get_itinerary(db, id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

from sqlalchemy.orm import Session
from app import models, schemas

# Create an itinerary and days
def create_itinerary(db: Session, itinerary: schemas.ItineraryCreate):
    # Create a itinerary record
    db_itinerary = models.Itinerary(
        name=itinerary.name,
        region=itinerary.region,
        nights=itinerary.nights
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)

    for day in itinerary.days:
        db_day = models.Day(
            itinerary_id=db_itinerary.id,
            day_number=day.day_number,
            hotel_name=day.hotel_name,
            hotel_location=day.hotel_location,
            activities=day.activities,
            transfer_mode=day.transfer_mode,
            transfer_from_location=day.transfer_from_location,
            transfer_to_location=day.transfer_to_location
        )
        db.add(db_day)

    db.commit()
    return db_itinerary

# Get all itineraries
def get_itineraries(db: Session):
    return db.query(models.Itinerary).all()

# Get a single itinerary by id
def get_itinerary(db: Session, itinerary_id: int):
    return db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()

def update_itinerary(db: Session, itinerary_id: int, itinerary: schemas.ItineraryCreate):
    db_itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()

    if db_itinerary:
        db_itinerary.name = itinerary.name
        db_itinerary.region = itinerary.region
        db_itinerary.nights = itinerary.nights

        db.commit()
        db.refresh(db_itinerary)

    return db_itinerary

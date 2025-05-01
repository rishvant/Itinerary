from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Itinerary model
class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String)
    nights = Column(Integer)

    days = relationship("Day", back_populates="itinerary")

# Day model
class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer)
    hotel_name = Column(String)
    hotel_location = Column(String)
    activities = Column(String)
    transfer_mode = Column(String)
    transfer_from_location = Column(String)
    transfer_to_location = Column(String)

    itinerary = relationship("Itinerary", back_populates="days")

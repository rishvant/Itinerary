from pydantic import BaseModel
from typing import List, Optional

# Day Schema
class DayBase(BaseModel):
    day_number: int
    hotel_name: Optional[str]
    hotel_location: Optional[str]
    activities: Optional[str]
    transfer_mode: Optional[str]
    transfer_from_location: Optional[str]
    transfer_to_location: Optional[str]

class DayCreate(DayBase):
    pass

class Day(DayBase):
    id: int
    itinerary_id: int

    class Config:
        orm_mode = True

# Itinerary Schema
class ItineraryBase(BaseModel):
    name: str
    region: str
    nights: int

class ItineraryCreate(ItineraryBase):
    days: List[DayCreate]

class Itinerary(ItineraryBase):
    id: int
    days: List[Day]

    class Config:
        orm_mode = True

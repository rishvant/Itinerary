from fastapi import FastAPI
from app.routes import itineraries, mcp
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary API",
    description="API for managing travel itineraries and getting recommendations",
    version="1.0.0"
)

# Routers
app.include_router(itineraries.router, prefix="/api", tags=["Itineraries"])
app.include_router(mcp.router, prefix="/api", tags=["Recommendations"])

@app.get("/")
def read_root():
    return {"message": "Server is running"}

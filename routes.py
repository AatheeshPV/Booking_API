from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas, models
from utils import convert_ist_to_timezone
import pytz

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/classes", response_model=list[schemas.ClassResponse])
def get_classes(timezone: str = Query("Asia/Kolkata"), db: Session = Depends(get_db)):
    try:
        pytz.timezone(timezone)
    except:
        raise HTTPException(status_code=400, detail="Invalid timezone")
    classes = db.query(models.FitnessClass).all()
    for c in classes:
        c.datetime = convert_ist_to_timezone(c.datetime, timezone)
    return classes

@router.post("/book", response_model=schemas.BookingResponse)
def book_class(req: schemas.BookingRequest, db: Session = Depends(get_db)):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == req.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    booking = models.Booking(**req.dict())
    fitness_class.available_slots -= 1
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(email: str, db: Session = Depends(get_db)):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()
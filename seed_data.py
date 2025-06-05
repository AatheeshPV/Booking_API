from sqlalchemy.orm import Session
from models import FitnessClass
from datetime import datetime, timedelta

def seed_classes(db: Session):
    if db.query(FitnessClass).first():
        return
    classes = [
        FitnessClass(name="Yoga", instructor="Aditi", datetime=datetime.now() + timedelta(days=1), available_slots=5),
        FitnessClass(name="Zumba", instructor="Raj", datetime=datetime.now() + timedelta(days=2), available_slots=3),
        FitnessClass(name="HIIT", instructor="Maya", datetime=datetime.now() + timedelta(days=3), available_slots=4),
    ]
    db.add_all(classes)
    db.commit()
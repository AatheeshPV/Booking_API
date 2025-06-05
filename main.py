from fastapi import FastAPI
from database import Base, engine, SessionLocal
from routes import router
from seed_data import seed_classes

app = FastAPI(title="🏋️ Fitness Class Booking API")

Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    seed_classes(db)

app.include_router(router)
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base
from routes import get_db
from seed_data import seed_classes

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)
with TestingSessionLocal() as db:
    seed_classes(db)

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes?timezone=Asia/Kolkata")
    assert response.status_code == 200
    assert "name" in response.json()[0]

def test_book_success():
    response = client.post("/book", json={
        "class_id": 1,
        "client_name": "Tester",
        "client_email": "test@mail.com"
    })
    assert response.status_code == 200

def test_book_not_found():
    response = client.post("/book", json={
        "class_id": 999,
        "client_name": "Ghost",
        "client_email": "ghost@mail.com"
    })
    assert response.status_code == 404

def test_book_overbooking():
    for i in range(3):  # Assuming Zumba has 3 slots
        client.post("/book", json={
            "class_id": 2,
            "client_name": f"User{i}",
            "client_email": f"user{i}@mail.com"
        })
    response = client.post("/book", json={
        "class_id": 2,
        "client_name": "Over",
        "client_email": "over@mail.com"
    })
    assert response.status_code == 400

def test_get_bookings():
    email = "repeat@mail.com"
    client.post("/book", json={
        "class_id": 1,
        "client_name": "Repeat",
        "client_email": email
    })
    response = client.get(f"/bookings?email={email}")
    assert response.status_code == 200
    assert email in response.text
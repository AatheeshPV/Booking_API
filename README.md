# 🏋️‍♂️ Fitness Studio Booking API

This project is a simple RESTful API built with **FastAPI** to simulate a booking system for a fictional fitness studio. It allows users to:

- View available fitness classes
- Book a spot in a class
- Retrieve bookings by email
- Automatically adjust class times based on timezone

---

## 📌 Project Features

✅ Built with **FastAPI**  
✅ Lightweight database using **SQLite**  
✅ Timezone-aware class scheduling (converts IST to user-specified timezone)  
✅ Full input validation with **Pydantic**  
✅ Clean modular structure following **DRY** principles  
✅ Unit tested using **pytest + FastAPI TestClient**  
✅ Ready for deployment and demo

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| **FastAPI** | Web framework for building APIs |
| **SQLite** | Lightweight in-memory or file-based database |
| **SQLAlchemy** | ORM for database modeling |
| **Pydantic v2** | Data validation & serialization |
| **Uvicorn** | ASGI server for running FastAPI |
| **Pytest** | Testing framework |
| **Pytz** | Timezone conversion |
| **HTTPX** | For async HTTP testing (optional)

---

## 📁 Project Structure

fitness_booking_api/
├── main.py # App entry point
├── models.py # SQLAlchemy DB models
├── schemas.py # Pydantic models for request/response
├── routes.py # API routes
├── utils.py # Timezone helper
├── seed_data.py # Seed script for sample classes
├── database.py # DB setup
├── requirements.txt # Dependencies
├── README.md # Documentation
└── tests/
└── test_main.py # Pytest test cases


---

## 🚀 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fitness_booking_api.git
cd fitness_booking_api


pip install -r requirements.txt

uvicorn main:app --reload
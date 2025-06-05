from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class ClassBase(BaseModel):
    name: str
    instructor: str
    datetime: datetime
    available_slots: int

class ClassResponse(ClassBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    model_config = ConfigDict(from_attributes=True)
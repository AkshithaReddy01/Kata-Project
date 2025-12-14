from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SweetCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)


class SweetUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)


class SweetResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    quantity: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


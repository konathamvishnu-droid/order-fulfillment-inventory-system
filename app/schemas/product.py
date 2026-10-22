from datetime import datetime

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    sku: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    quantity: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )
    description: str | None = None
    quantity: int | None = Field(
        default=None,
        ge=0,
    )
    is_active: bool | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None
    quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
from datetime import datetime

from pydantic import BaseModel, Field


class StockMovementCreate(BaseModel):
    product_id: int = Field(..., gt=0)

    movement_type: str = Field(
        ...,
        pattern="^(IN|OUT)$",
    )

    quantity: int = Field(
        ...,
        gt=0,
    )

    reason: str | None = None


class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    movement_type: str
    quantity: int
    reason: str | None
    created_at: datetime

    class Config:
        from_attributes = True
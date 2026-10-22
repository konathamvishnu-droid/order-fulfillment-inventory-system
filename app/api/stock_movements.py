from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.stock_movement import (
    StockMovementCreate,
    StockMovementResponse,
)
from app.services.stock_movement_service import (
    create_stock_movement_service,
    get_product_stock_movements_service,
)


router = APIRouter(
    prefix="/stock-movements",
    tags=["Stock Movements"],
)


@router.post(
    "",
    response_model=StockMovementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_stock_movement(
    movement_data: StockMovementCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        return create_stock_movement_service(
            db=db,
            product_id=movement_data.product_id,
            movement_type=movement_data.movement_type,
            quantity=movement_data.quantity,
            reason=movement_data.reason,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get(
    "/product/{product_id}",
    response_model=list[StockMovementResponse],
)
def get_product_stock_movements(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        return get_product_stock_movements_service(
            db=db,
            product_id=product_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
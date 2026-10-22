from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.stock_movement import StockMovement


def create_stock_movement(
    db: Session,
    product_id: int,
    movement_type: str,
    quantity: int,
    reason: str | None = None,
):
    movement = StockMovement(
        product_id=product_id,
        movement_type=movement_type,
        quantity=quantity,
        reason=reason,
    )

    db.add(movement)
    db.commit()
    db.refresh(movement)

    return movement


def get_stock_movements_by_product(
    db: Session,
    product_id: int,
):
    statement = (
        select(StockMovement)
        .where(StockMovement.product_id == product_id)
        .order_by(StockMovement.id.desc())
    )

    return db.execute(statement).scalars().all()
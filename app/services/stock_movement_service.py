from sqlalchemy.orm import Session

from app.repositories.product_repository import get_product_by_id
from app.repositories.stock_movement_repository import (
    create_stock_movement,
)


def create_stock_movement_service(
    db: Session,
    product_id: int,
    movement_type: str,
    quantity: int,
    reason: str | None = None,
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    if not product.is_active:
        raise ValueError("Product is inactive")

    if movement_type == "IN":
        product.quantity += quantity

    elif movement_type == "OUT":
        if product.quantity < quantity:
            raise ValueError("Insufficient stock")

        product.quantity -= quantity

    else:
        raise ValueError("Movement type must be IN or OUT")

    db.commit()
    db.refresh(product)

    movement = create_stock_movement(
        db=db,
        product_id=product_id,
        movement_type=movement_type,
        quantity=quantity,
        reason=reason,
    )

    return movement


def get_product_stock_movements_service(
    db: Session,
    product_id: int,
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    from app.repositories.stock_movement_repository import (
        get_stock_movements_by_product,
    )

    return get_stock_movements_by_product(
        db=db,
        product_id=product_id,
    )
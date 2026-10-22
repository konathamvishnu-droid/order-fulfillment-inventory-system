from sqlalchemy.orm import Session

from app.repositories.product_repository import (
    create_product,
    delete_product,
    get_product_by_id,
    get_product_by_sku,
    get_products,
    update_product,
)


def create_product_service(
    db: Session,
    name: str,
    sku: str,
    description: str | None,
    quantity: int,
):
    existing_product = get_product_by_sku(db, sku)

    if existing_product:
        raise ValueError("SKU already exists")

    return create_product(
        db=db,
        name=name,
        sku=sku,
        description=description,
        quantity=quantity,
    )


def get_product_service(
    db: Session,
    product_id: int,
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return product


def get_all_products_service(
    db: Session,
):
    return get_products(db)


def update_product_service(
    db: Session,
    product_id: int,
    name: str | None = None,
    description: str | None = None,
    quantity: int | None = None,
    is_active: bool | None = None,
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return update_product(
        db=db,
        product=product,
        name=name,
        description=description,
        quantity=quantity,
        is_active=is_active,
    )


def delete_product_service(
    db: Session,
    product_id: int,
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    delete_product(db, product)
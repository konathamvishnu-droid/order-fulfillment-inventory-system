from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


def get_product_by_id(
    db: Session,
    product_id: int,
):
    statement = select(Product).where(
        Product.id == product_id
    )

    return db.execute(statement).scalar_one_or_none()


def get_product_by_sku(
    db: Session,
    sku: str,
):
    statement = select(Product).where(
        Product.sku == sku
    )

    return db.execute(statement).scalar_one_or_none()


def get_products(
    db: Session,
):
    statement = select(Product).order_by(Product.id)

    return db.execute(statement).scalars().all()


def create_product(
    db: Session,
    name: str,
    sku: str,
    description: str | None,
    quantity: int,
):
    product = Product(
        name=name,
        sku=sku,
        description=description,
        quantity=quantity,
        is_active=True,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def update_product(
    db: Session,
    product: Product,
    name: str | None = None,
    description: str | None = None,
    quantity: int | None = None,
    is_active: bool | None = None,
):
    if name is not None:
        product.name = name

    if description is not None:
        product.description = description

    if quantity is not None:
        product.quantity = quantity

    if is_active is not None:
        product.is_active = is_active

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product: Product,
):
    db.delete(product)
    db.commit()
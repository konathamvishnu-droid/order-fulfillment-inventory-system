from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)


def register_user(
    db: Session,
    name: str,
    email: str,
    password: str,
):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise ValueError("Email already registered")

    password_hashed = hash_password(password)

    return create_user(
        db=db,
        name=name,
        email=email,
        password_hash=password_hashed,
        role="customer",
    )


def login_user(
    db: Session,
    email: str,
    password: str,
):
    user = get_user_by_email(db, email)

    if not user:
        raise ValueError("Invalid email or password")

    if not user.is_active:
        raise ValueError("User account is inactive")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password")

    access_token = create_access_token(
        user_id=user.id,
        role=user.role,
    )

    return access_token
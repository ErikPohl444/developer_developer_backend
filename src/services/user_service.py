from fastapi import HTTPException
from sqlmodel import Session
from src.models.user import User
from src.services.generic_return_all_items_service import read_all_items_service


def create_user_service(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return {
        "message": f"User {user.name} created successfully!",
        "data": user
    }


def read_user_service(user_id: int, session: Session):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def read_all_users_service(session: Session):
    return read_all_items_service(session, User)

from fastapi import HTTPException
from sqlmodel import Session
from src.models.user import User

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
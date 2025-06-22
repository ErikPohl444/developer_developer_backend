from fastapi import HTTPException
from sqlmodel import Session
from src.models.role import Role

def create_role_service(role: Role, session: Session):
    session.add(role)
    session.commit()
    session.refresh(role)
    return {
        "message": f"Role {role.name} created successfully!",
        "data": role
    }

def read_role_service(role_id: int, session: Session):
    role = session.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role
from fastapi import HTTPException
from sqlmodel import Session, select
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


def read_all_roles_service(session: Session):
    with session:
        statement = select(Role)
        roles = session.exec(statement)
        if not roles:
            raise HTTPException(status_code=404, detail="Roles not found")
        all_roles = roles.all()
    return all_roles

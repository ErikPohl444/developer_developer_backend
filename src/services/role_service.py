from sqlmodel import Session
from src.models.role import Role
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_role_service(role: Role, session: Session):
    return create_item_service(session, role)


def read_role_service(role_id: int, session: Session):
    return return_one_item_service(Role, role_id, session)


def read_all_roles_service(session: Session):
    return read_all_items_service(session, Role)

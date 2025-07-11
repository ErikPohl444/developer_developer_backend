from sqlmodel import Session
from src.models.user import User
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_user_service(user: User, session: Session):
    return create_item_service(session, user)


def read_user_service(user_id: int, session: Session):
    return return_one_item_service(User, user_id, session)


def read_all_users_service(session: Session):
    return read_all_items_service(session, User)

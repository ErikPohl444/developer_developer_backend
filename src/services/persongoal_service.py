from sqlmodel import Session
from src.models.persongoal import PersonGoal
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_persongoal_service(persongoal: PersonGoal, session: Session):
    return create_item_service(session, persongoal)


def read_persongoal_service(persongoal_id: int, session: Session):
    return return_one_item_service(PersonGoal, persongoal_id, session)


def read_all_persongoals_service(session: Session):
    return read_all_items_service(session, PersonGoal)

from sqlmodel import Session
from src.models.personskillhistory import PersonSkillHistory
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_personskillhistory_service(personskillhistory: PersonSkillHistory, session: Session):
    return create_item_service(session, personskillhistory)


def read_personskillhistory_service(personskillhistory_id: int, session: Session):
    return return_one_item_service(PersonSkillHistory, personskillhistory_id, session)


def read_all_personskillhistories_service(session: Session):
    return read_all_items_service(session, PersonSkillHistory)

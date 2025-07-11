from sqlmodel import Session
from src.models.personskill import PersonSkill
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_personskill_service(personskill: PersonSkill, session: Session):
    return create_item_service(session, personskill)


def read_personskill_service(personskill_id: int, session: Session):
    return return_one_item_service(PersonSkill, personskill_id, session)


def read_all_personskills_service(session: Session):
    return read_all_items_service(session, PersonSkill)

from sqlmodel import Session
from src.models.person import Person
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_person_service(person: Person, session: Session):
    return create_item_service(session, person)


def read_person_service(person_id: int, session: Session):
    return return_one_item_service(Person, person_id, session)


def read_all_persons_service(session: Session):
    return read_all_items_service(session, Person)

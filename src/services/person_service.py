from fastapi import HTTPException
from sqlmodel import Session
from src.models.person import Person
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_person_service(person: Person, session: Session):
    return create_item_service(session, person)


def read_person_service(person_id: int, session: Session):
    person = session.get(Person, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


def read_all_persons_service(session: Session):
    return read_all_items_service(session, Person)

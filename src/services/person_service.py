from fastapi import HTTPException
from sqlmodel import Session
from src.models.person import Person

def create_person_service(person: Person, session: Session):
    session.add(person)
    session.commit()
    session.refresh(person)
    return {
        "message": f"Person {person.name} created successfully!",
        "data": person
    }

def read_person_service(person_id: int, session: Session):
    person = session.get(Person, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person
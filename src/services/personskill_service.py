from fastapi import HTTPException
from sqlmodel import Session
from src.models.personskill import PersonSkill
from src.services.generic_return_all_items_service import read_all_items_service


def create_personskill_service(personskill: PersonSkill, session: Session):
    session.add(personskill)
    session.commit()
    session.refresh(personskill)
    return {
        "message": f"PersonSkill {personskill.name} created successfully!",
        "data": personskill
    }


def read_personskill_service(personskill_id: int, session: Session):
    personskill = session.get(PersonSkill, personskill_id)
    if not personskill:
        raise HTTPException(status_code=404, detail="PersonSkill not found")
    return personskill


def read_all_personskills_service(session: Session):
    return read_all_items_service(session, PersonSkill)

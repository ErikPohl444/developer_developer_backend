from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.personskill import PersonSkill


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
    with session:
        statement = select(PersonSkill)
        personskills = session.exec(statement)
        if not personskills:
            raise HTTPException(status_code=404, detail="PersonSkills not found")
        all_personskills = personskills.all()
    return all_personskills

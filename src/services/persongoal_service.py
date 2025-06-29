from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.persongoal import PersonGoal


def create_persongoal_service(persongoal: PersonGoal, session: Session):
    session.add(persongoal)
    session.commit()
    session.refresh(persongoal)
    return {
        "message": f"PersonGoal {persongoal.name} created successfully!",
        "data": persongoal
    }


def read_persongoal_service(persongoal_id: int, session: Session):
    persongoal = session.get(PersonGoal, persongoal_id)
    if not persongoal:
        raise HTTPException(status_code=404, detail="PersonGoal not found")
    return persongoal


def read_all_persongoals_service(session: Session):
    with session:
        statement = select(PersonGoal)
        persongoals = session.exec(statement)
        if not persongoals:
            raise HTTPException(status_code=404, detail="PersonSkills not found")
        all_persongoals = persongoals.all()
    return all_persongoals

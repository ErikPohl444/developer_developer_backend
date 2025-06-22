from fastapi import HTTPException
from sqlmodel import Session
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
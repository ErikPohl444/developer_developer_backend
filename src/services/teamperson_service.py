from fastapi import HTTPException
from sqlmodel import Session
from src.models.teamperson import TeamPerson
from src.services.generic_return_all_items_service import read_all_items_service


def create_teamperson_service(teamperson: TeamPerson, session: Session):
    session.add(teamperson)
    session.commit()
    session.refresh(teamperson)
    return {
        "message": f"TeamPerson {teamperson.name} created successfully!",
        "data": teamperson
    }


def read_teamperson_service(teamperson_id: int, session: Session):
    teamperson = session.get(TeamPerson, teamperson_id)
    if not teamperson:
        raise HTTPException(status_code=404, detail="TeamPerson not found")
    return teamperson_id


def read_all_teampersons_service(session: Session):
    return read_all_items_service(session, TeamPerson)

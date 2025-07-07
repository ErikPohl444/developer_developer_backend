from fastapi import HTTPException
from sqlmodel import Session
from src.models.teamperson import TeamPerson
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_teamperson_service(teamperson: TeamPerson, session: Session):
    return create_item_service(session, teamperson)


def read_teamperson_service(teamperson_id: int, session: Session):
    teamperson = session.get(TeamPerson, teamperson_id)
    if not teamperson:
        raise HTTPException(status_code=404, detail="TeamPerson not found")
    return teamperson_id


def read_all_teampersons_service(session: Session):
    return read_all_items_service(session, TeamPerson)

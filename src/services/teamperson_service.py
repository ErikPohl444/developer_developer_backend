from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.teamperson import TeamPerson


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
    with session:
        statement = select(TeamPerson)
        teampersons = session.exec(statement)
        if not teampersons:
            raise HTTPException(status_code=404, detail="TeamPersons not found")
        all_teampersons = teampersons.all()
    return all_teampersons

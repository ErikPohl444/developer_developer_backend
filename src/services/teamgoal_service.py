from fastapi import HTTPException
from sqlmodel import Session
from src.models.teamgoal import TeamGoal
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_teamgoal_service(teamgoal: TeamGoal, session: Session):
    return create_item_service(session, teamgoal)


def read_teamgoal_service(teamgoal_id: int, session: Session):
    teamgoal = session.get(TeamGoal, teamgoal_id)
    if not teamgoal:
        raise HTTPException(status_code=404, detail="TeamGoal not found")
    return teamgoal


def read_all_teamgoals_service(session: Session):
    return read_all_items_service(session, TeamGoal)

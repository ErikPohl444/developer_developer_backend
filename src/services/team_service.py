from fastapi import HTTPException
from sqlmodel import Session
from src.models.team import Team
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_team_service(team: Team, session: Session):
    return create_item_service(session, team)


def read_team_service(team_id: int, session: Session):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


def read_all_teams_service(session: Session):
    return read_all_items_service(session, Team)

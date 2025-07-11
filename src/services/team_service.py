from sqlmodel import Session
from src.models.team import Team
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_team_service(team: Team, session: Session):
    return create_item_service(session, team)


def read_team_service(team_id: int, session: Session):
    return return_one_item_service(Team, team_id, session)


def read_all_teams_service(session: Session):
    return read_all_items_service(session, Team)

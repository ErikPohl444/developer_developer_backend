from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.team import Team


def create_team_service(team: Team, session: Session):
    session.add(team)
    session.commit()
    session.refresh(team)
    return {
        "message": f"Team {team.name} created successfully!",
        "data": team
    }


def read_team_service(team_id: int, session: Session):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


def read_all_teams_service(session: Session):
    with session:
        statement = select(Team)
        teams = session.exec(statement)
        if not teams:
            raise HTTPException(status_code=404, detail="Teams not found")
        all_teams = teams.all()
    return all_teams

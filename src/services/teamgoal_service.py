from fastapi import HTTPException
from sqlmodel import Session
from src.models.teamgoal import TeamGoal

def create_teamgoal_service(teamgoal: TeamGoal, session: Session):
    session.add(teamgoal)
    session.commit()
    session.refresh(teamgoal)
    return {
        "message": f"TeamGoal {teamgoal.name} created successfully!",
        "data": teamgoal
    }

def read_teamgoal_service(teamgoal_id: int, session: Session):
    teamgoal = session.get(TeamGoal, teamgoal_id)
    if not teamgoal:
        raise HTTPException(status_code=404, detail="TeamGoal not found")
    return teamgoal
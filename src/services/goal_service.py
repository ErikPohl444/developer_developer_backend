from fastapi import HTTPException
from sqlmodel import Session
from src.models.goal import Goal

def create_goal_service(goal: Goal, session: Session):
    session.add(goal)
    session.commit()
    session.refresh(goal)
    return {
        "message": f"Goal {goal.name} created successfully!",
        "data": goal
    }

def read_goal_service(goal_id: int, session: Session):
    goal = session.get(Goal, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal
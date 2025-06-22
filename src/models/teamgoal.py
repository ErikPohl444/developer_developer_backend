from sqlmodel import SQLModel
import datetime

class TeamGoal(SQLModel):
    goal_id: int
    team_id: int
    max_team_score_exceeds: int
    avg_score: int
    due_date: datetime.date
from sqlmodel import SQLModel
import datetime


class TeamGoal(SQLModel, table=True):
    teamgoal_id: int | None = Field(default=None, primary_key=True)
    goal_id: int
    team_id: int
    max_team_score_exceeds: int
    avg_score: int
    due_date: datetime.date

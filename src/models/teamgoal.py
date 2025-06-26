from sqlmodel import SQLModel, Field
import datetime


class TeamGoal(SQLModel, table=True):
    teamgoal_id: int | None = Field(default=None, primary_key=True)
    goal_id: int = Field(foreign_key="goal.goal_id")
    team_id: int = Field(foreign_key="team.team_id")
    max_team_score_exceeds: int
    avg_score: int
    due_date: datetime.date

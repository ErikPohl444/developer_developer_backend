from sqlmodel import SQLModel, Field
import datetime


class TeamGoal(SQLModel, table=True):
    """
    SQLModel TeamGoal
    Purpose: Set a target for a team and for a skill
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    teamgoal_id: int | None = Field(default=None, primary_key=True)
    skill_id: int = Field(foreign_key="skill.skill_id")
    team_id: int = Field(foreign_key="team.team_id")
    max_team_score_exceeds: int
    avg_score: int
    due_date: datetime.date

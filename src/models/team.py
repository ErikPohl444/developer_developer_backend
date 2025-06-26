from sqlmodel import SQLModel, Field
import datetime


class Team(SQLModel, table=True):
    """
    SQLModel Team
    Purpose: A team is a group of 1 or more persons and a team can have a parent team
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    team_id: int | None = Field(default=None, primary_key=True)
    parent_team_id: int = Field(foreign_key="team.team_id")
    name: str
    manager: int = Field(foreign_key="person.person_id")

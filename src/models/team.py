from sqlmodel import SQLModel, Field


class Team(SQLModel, table=True):
    team_id: int | None = Field(default=None, primary_key=True)
    parent_team_id: int
    name: str
    manager: int

from sqlmodel import SQLModel


class Team(SQLModel, table=True):
    team_id: int
    parent_team_id: int
    name: str
    manager: int

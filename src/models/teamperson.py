from sqlmodel import SQLModel, Field


class TeamPerson(SQLModel, table=True):
    teamperson_id: int | None = Field(default=None, primary_key=True)
    team_id: int
    person_id: int

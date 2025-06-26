from sqlmodel import SQLModel, Field


class TeamPerson(SQLModel, table=True):
    teamperson_id: int | None = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="team.team_id")
    person_id: int = Field(foreign_key="person.person_id")

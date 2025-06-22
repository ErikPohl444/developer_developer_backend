from sqlmodel import SQLModel


class TeamPerson(SQLModel):
    teamperson_id: int
    team_id: int
    person_id: int

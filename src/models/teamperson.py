from sqlmodel import SQLModel


class TeamPerson(SQLModel, table=True):
    teamperson_id: int
    team_id: int
    person_id: int

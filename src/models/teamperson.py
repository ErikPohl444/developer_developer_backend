from sqlmodel import SQLModel, Field
import datetime


class TeamPerson(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    teamperson_id: int | None = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="team.team_id")
    person_id: int = Field(foreign_key="person.person_id")

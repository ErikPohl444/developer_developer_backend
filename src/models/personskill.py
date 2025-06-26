from sqlmodel import SQLModel, Field
import datetime


class PersonSkill(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.date
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.date
    personskill_id: int | None = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.person_id")
    skill_id: int = Field(foreign_key="skill.skill_id")
    score: int

from sqlmodel import SQLModel


class PersonSkill(SQLModel, table=True):
    personskill_id: int
    person_id: int
    skill_id: int
    score: int

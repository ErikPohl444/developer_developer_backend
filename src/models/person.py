from sqlmodel import SQLModel


class Person(SQLModel):
    person_id: int
    name: str
    role_id: int

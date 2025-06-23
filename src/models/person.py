from sqlmodel import SQLModel


class Person(SQLModel, table=True):
    person_id: int
    name: str
    role_id: int

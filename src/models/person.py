from sqlmodel import SQLModel, Field


class Person(SQLModel, table=True):
    person_id: int | None = Field(default=None, primary_key=True)
    name: str
    role_id: int = Field(foreign_key="role.role_id")

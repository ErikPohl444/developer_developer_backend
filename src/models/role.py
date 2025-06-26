from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    role_id: int | None = Field(default=None, primary_key=True)
    name: str

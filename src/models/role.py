from sqlmodel import SQLModel


class Role(SQLModel, table=True):
    role_id: int
    name: str

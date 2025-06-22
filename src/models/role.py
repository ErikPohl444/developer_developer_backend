from sqlmodel import SQLModel


class Role(SQLModel):
    role_id: int
    name: str

from sqlmodel import SQLModel


class Tool(SQLModel):
    tool_id: int
    tool_name: str

from sqlmodel import SQLModel


class Tool(SQLModel, table=True):
    tool_id: int
    tool_name: str

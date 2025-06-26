from sqlmodel import SQLModel, Field


class Tool(SQLModel, table=True):
    tool_id: int | None = Field(default=None, primary_key=True)
    tool_name: str
    tool_uri: str

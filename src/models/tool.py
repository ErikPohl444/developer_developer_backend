from sqlmodel import SQLModel, Field
import datetime


class Tool(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.date
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.date
    tool_id: int | None = Field(default=None, primary_key=True)
    tool_name: str
    tool_uri: str

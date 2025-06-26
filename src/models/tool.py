from sqlmodel import SQLModel, Field
import datetime


class Tool(SQLModel, table=True):
    """
    SQLModel Tool
    Purpose: A tool is something which can be used to improve a skill
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    tool_id: int | None = Field(default=None, primary_key=True)
    tool_name: str
    tool_description: str
    tool_uri: str

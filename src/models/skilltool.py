from sqlmodel import SQLModel, Field
import datetime


class SkillTool(SQLModel, table=True):
    """
    SQLModel SkillTool
    Purpose: Relate skills to tools which improve those skills
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    skilltool_id: int | None = Field(default=None, primary_key=True)
    tool_id: int = Field(foreign_key="tool.tool_id")
    skill_id: int = Field(foreign_key="skill.skill_id")

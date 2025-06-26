from sqlmodel import SQLModel, Field


class SkillTool(SQLModel, table=True):
    skilltool_id: int | None = Field(default=None, primary_key=True)
    tool_id: int
    skill_id: int

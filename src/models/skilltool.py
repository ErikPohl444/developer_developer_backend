from sqlmodel import SQLModel


class SkillTool(SQLModel):
    skilltool_id: int
    tool_id: int
    skill_id: int

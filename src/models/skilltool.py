from sqlmodel import SQLModel


class SkillTool(SQLModel, table=True):
    skilltool_id: int
    tool_id: int
    skill_id: int

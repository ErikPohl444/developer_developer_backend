from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.skilltool import SkillTool


def create_skilltool_service(skilltool: SkillTool, session: Session):
    session.add(skilltool)
    session.commit()
    session.refresh(skilltool)
    return {
        "message": f"SkillTool {skilltool.name} created successfully!",
        "data": skilltool
    }


def read_skilltool_service(skilltool_id: int, session: Session):
    skilltool = session.get(SkillTool, skilltool_id)
    if not skilltool:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skilltool


def read_all_skilltools_service(session: Session):
    with session:
        statement = select(SkillTool)
        skilltools = session.exec(statement)
        if not skilltools:
            raise HTTPException(status_code=404, detail="SkillTools not found")
        all_skilltools = skilltools.all()
    return all_skilltools

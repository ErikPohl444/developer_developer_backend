from fastapi import HTTPException
from sqlmodel import Session
from src.models.skilltool import SkillTool
from src.services.generic_return_all_items_service import read_all_items_service


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
    return read_all_items_service(session, SkillTool)

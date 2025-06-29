from fastapi import HTTPException
from sqlmodel import Session, select
from src.models.skill import Skill


def create_skill_service(skill: Skill, session: Session):
    session.add(skill)
    session.commit()
    session.refresh(skill)
    return {
        "message": f"Skill {skill.name} created successfully!",
        "data": skill
    }


def read_skill_service(skill_id: int, session: Session):
    skill = session.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


def read_all_skills_service(session: Session):
    with session:
        statement = select(Skill)
        skills = session.exec(statement)
        if not skills:
            raise HTTPException(status_code=404, detail="Skills not found")
        all_skills = skills.all()
    return all_skills

from fastapi import HTTPException
from sqlmodel import Session
from src.models.skill import Skill
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_skill_service(skill: Skill, session: Session):
    return create_item_service(session, skill)


def read_skill_service(skill_id: int, session: Session):
    skill = session.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


def read_all_skills_service(session: Session):
    return read_all_items_service(session, Skill)

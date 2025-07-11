from sqlmodel import Session
from src.models.skill import Skill
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_skill_service(skill: Skill, session: Session):
    return create_item_service(session, skill)


def read_skill_service(skill_id: int, session: Session):
    return return_one_item_service(Skill, skill_id, session)


def read_all_skills_service(session: Session):
    return read_all_items_service(session, Skill)

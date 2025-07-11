from sqlmodel import Session
from src.models.skilltool import SkillTool
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service
from src.services.generic_return_one_item_service import return_one_item_service


def create_skilltool_service(skilltool: SkillTool, session: Session):
    return create_item_service(session, skilltool)


def read_skilltool_service(skilltool_id: int, session: Session):
    return return_one_item_service(SkillTool, skilltool_id, session)


def read_all_skilltools_service(session: Session):
    return read_all_items_service(session, SkillTool)

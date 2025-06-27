from src.models.skill import Skill
from src.services.skill_service import create_skill_service, read_skill_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=Skill,
    create_service=create_skill_service,
    read_service=read_skill_service,
    resource_name="skills",
    session_dep=SessionDep,
    get_session_func=get_session,
)

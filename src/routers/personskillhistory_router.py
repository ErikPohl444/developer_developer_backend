from src.models.personskillhistory import PersonSkillHistory
from src.services.personskillhistory_service import create_personskillhistory_service, read_personskillhistory_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=PersonSkillHistory,
    create_service=create_personskillhistory_service,
    read_service=read_personskillhistory_service,
    resource_name="personskillhistories",
    session_dep=SessionDep,
    get_session_func=get_session,
)

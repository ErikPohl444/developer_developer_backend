from src.models.personskill import PersonSkill
from src.services.personskill_service import create_personskill_service, read_personskill_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=PersonSkill,
    create_service=create_personskill_service,
    read_service=read_personskill_service,
    resource_name="personskills",
    session_dep=SessionDep,
    get_session_func=get_session,
)

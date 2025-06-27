from src.models.persongoal import PersonGoal
from src.services.persongoal_service import create_persongoal_service, read_persongoal_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=PersonGoal,
    create_service=create_persongoal_service,
    read_service=read_persongoal_service,
    resource_name="persongoals",
    session_dep=SessionDep,
    get_session_func=get_session,
)

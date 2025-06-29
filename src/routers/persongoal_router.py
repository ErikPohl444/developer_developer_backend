from src.models.persongoal import PersonGoal
from src.services.persongoal_service import create_persongoal_service, read_persongoal_service, read_all_persongoals_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=PersonGoal,
    create_service=create_persongoal_service,
    read_service=read_persongoal_service,
    read_all_service=read_all_persongoals_service,
    resource_name="persongoals",
    session_dep=SessionDep,
)

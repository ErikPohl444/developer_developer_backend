from src.models.teamgoal import TeamGoal
from src.services.teamgoal_service import create_teamgoal_service, read_teamgoal_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=TeamGoal,
    create_service=create_teamgoal_service,
    read_service=read_teamgoal_service,
    resource_name="teamgoals",
    session_dep=SessionDep,
)

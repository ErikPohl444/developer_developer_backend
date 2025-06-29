from src.models.team import Team
from src.services.team_service import create_team_service, read_team_service, read_all_teams_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=Team,
    create_service=create_team_service,
    read_service=read_team_service,
    read_all_service=read_all_teams_service,
    resource_name="teams",
    session_dep=SessionDep,
)

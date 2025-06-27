from src.models.team import Team
from src.services.team_service import create_team_service, read_team_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=Team,
    create_service=create_team_service,
    read_service=read_team_service,
    resource_name="teams",
    session_dep=SessionDep,
    get_session_func=get_session,
)

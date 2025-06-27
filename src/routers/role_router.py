from src.models.role import Role
from src.services.role_service import create_role_service, read_role_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=Role,
    create_service=create_role_service,
    read_service=read_role_service,
    resource_name="roles",
    session_dep=SessionDep,
    get_session_func=get_session,
)

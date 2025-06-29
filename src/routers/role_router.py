from src.models.role import Role
from src.services.role_service import create_role_service, read_role_service, read_all_roles_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=Role,
    create_service=create_role_service,
    read_service=read_role_service,
    read_all_service=read_all_roles_service,
    resource_name="roles",
    session_dep=SessionDep,
)

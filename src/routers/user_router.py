from src.models.user import User
from src.services.user_service import create_user_service, read_user_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=User,
    create_service=create_user_service,
    read_service=read_user_service,
    resource_name="users",
    session_dep=SessionDep,
    get_session_func=get_session,
)

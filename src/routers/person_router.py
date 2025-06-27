from src.models.person import Person
from src.services.person_service import create_person_service, read_person_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router



router = create_crud_router(
    model=Person,
    create_service=create_person_service,
    read_service=read_person_service,
    resource_name="persons",
    session_dep=SessionDep,
    get_session_func=get_session,
)

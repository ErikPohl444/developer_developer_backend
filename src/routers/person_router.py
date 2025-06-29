from src.models.person import Person
from src.services.person_service import create_person_service, read_person_service, read_all_persons_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=Person,
    create_service=create_person_service,
    read_service=read_person_service,
    read_all_service=read_all_persons_service,
    resource_name="persons",
    session_dep=SessionDep,
)

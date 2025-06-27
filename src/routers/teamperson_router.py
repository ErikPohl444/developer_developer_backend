from src.models.teamperson import TeamPerson
from src.services.teamperson_service import create_teamperson_service, read_teamperson_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=TeamPerson,
    create_service=create_teamperson_service,
    read_service=read_teamperson_service,
    resource_name="teampersons",
    session_dep=SessionDep,
)

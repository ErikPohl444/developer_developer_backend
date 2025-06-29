from src.models.personskill import PersonSkill
from src.services.personskill_service import create_personskill_service, read_personskill_service, read_all_personskills_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=PersonSkill,
    create_service=create_personskill_service,
    read_service=read_personskill_service,
    read_all_service=read_all_personskills_service,
    resource_name="personskills",
    session_dep=SessionDep,
)

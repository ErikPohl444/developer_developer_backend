from src.models.skilltool import SkillTool
from src.services.skilltool_service import create_skilltool_service, read_skilltool_service, read_all_skilltools_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=SkillTool,
    create_service=create_skilltool_service,
    read_service=read_skilltool_service,
    read_all_service=read_all_skilltools_service,
    resource_name="skilltools",
    session_dep=SessionDep,
)

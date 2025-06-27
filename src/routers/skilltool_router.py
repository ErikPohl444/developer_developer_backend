from src.models.skilltool import SkillTool
from src.services.skilltool_service import create_skilltool_service, read_skilltool_service
from src.main import SessionDep, get_session
from generic_router_factory import create_crud_router


router = create_crud_router(
    model=SkillTool,
    create_service=create_skilltool_service,
    read_service=read_skilltool_service,
    resource_name="skilltools",
    session_dep=SessionDep,
    get_session_func=get_session,
)

from src.models.tool import Tool
from src.services.tool_service import create_tool_service, read_tool_service, read_all_tools_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=Tool,
    create_service=create_tool_service,
    read_service=read_tool_service,
    read_all_service=read_all_tools_service,
    resource_name="tools",
    session_dep=SessionDep,
)

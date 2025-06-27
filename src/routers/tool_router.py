from fastapi import APIRouter, Depends
from src.models.tool import Tool
from src.services.tool_service import create_tool_service, read_tool_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-tool/")
@version(1, 0)
def create_tool(tool: Tool, session: SessionDep = Depends(get_session)):
    """Create a tool."""
    return create_tool_service(tool, session)


@router.get("/tools/{tool_id}")
@version(1, 0)
async def read_tool(tool_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a tool by its ID."""
    return read_tool_service(tool_id, session)

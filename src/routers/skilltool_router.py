from src.models.skilltool import SkillTool
from src.services.skilltool_service import create_skilltool_service, read_skilltool_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/skilltools/")
@version(1, 0)
def create_skilltool(skilltool: SkillTool, session: SessionDep = Depends(get_session)):
    """Create a skilltool."""
    return create_skilltool_service(skilltool, session)


@router.get("/skilltools/{skill_id}")
@version(1, 0)
async def read_skilltool(skilltool_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a skilltool by its ID."""
    return read_skilltool_service(skilltool_id, session)

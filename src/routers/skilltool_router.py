from fastapi import APIRouter, Depends
from src.models.skill import Skill
from src.services.skill_service import create_skill_service, read_skill_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-skill/")
@version(1, 0)
def create_skill(skill: Skill, session: SessionDep = Depends(get_session)):
    """Create a skilltool."""
    return create_skill_service(skill, session)


@router.get("/skills/{skill_id}")
@version(1, 0)
async def read_skill(skill_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a skilltool by its ID."""
    return read_skill_service(skill_id, session)

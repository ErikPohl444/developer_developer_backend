from fastapi import APIRouter, Depends
from src.models.personskill import PersonSkill
from src.services.personskill_service import create_personskill_service, read_personskill_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-personskill/")
@version(1, 0)
def create_personskill(personskill: PersonSkill, session: SessionDep = Depends(get_session)):
    """Retrieve a personskill by its ID."""
    return create_personskill_service(personskill, session)


@router.get("/personskills/{personskill_id}")
@version(1, 0)
async def read_personskill(personskill_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a personskill by their ID."""
    return read_personskill_service(personskill_id, session)

from src.models.personskillhistory import PersonSkillHistory
from src.services.personskillhistory_service import create_personskillhistory_service, read_personskillhistory_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/personskillhistories/")
@version(1, 0)
def create_personskillhistory(personskillhistory: PersonSkillHistory, session: SessionDep = Depends(get_session)):
    """Create a personskilhistory entry."""
    return create_personskillhistory_service(personskillhistory, session)


@router.get("/personskillhistories/{personskillhistory_id}")
@version(1, 0)
async def read_personskillhistories(personskillhistory_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a personskilhistory by its ID."""
    return read_personskillhistory_service(personskillhistory_id, session)

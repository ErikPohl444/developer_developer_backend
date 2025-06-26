from fastapi import APIRouter, Depends
from src.models.persongoal import PersonGoal
from src.services.persongoal_service import create_persongoal_service, read_persongoal_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-persongoal/")
@version(1, 0)
def create_persongoal(persongoal: PersonGoal, session: SessionDep = Depends(get_session)):
    return create_persongoal_service(persongoal, session)


@router.get("/persongoals/{persongoal_id}")
@version(1, 0)
async def read_persongoal(persongoal_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_persongoal_service(persongoal_id, session)

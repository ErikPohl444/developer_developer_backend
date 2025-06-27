from src.models.teamgoal import TeamGoal
from src.services.teamgoal_service import create_teamgoal_service, read_teamgoal_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/teampgoals/")
@version(1, 0)
def create_teamgoal(teamgoal: TeamGoal, session: SessionDep = Depends(get_session)):
    """Create a teamgoal."""
    return create_teamgoal_service(teamgoal, session)


@router.get("/teamgoals/{teamgoals_id}")
@version(1, 0)
async def read_teamgoal(teamgoal_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a teamgoal by its ID."""
    return read_teamgoal_service(teamgoal_id, session)

from fastapi import APIRouter, Depends
from src.models.team import Team
from src.services.team_service import create_team_service, read_team_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-team/")
@version(1, 0)
def create_team(team: Team, session: SessionDep = Depends(get_session)):
    """Create a team."""
    return create_team_service(team, session)


@router.get("/teams/{team_id}")
@version(1, 0)
async def read_team(team_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a team by its ID."""
    return read_team_service(team_id, session)

from src.models.teamperson import TeamPerson
from src.services.teamperson_service import create_teamperson_service, read_teamperson_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/teampersons/")
@version(1, 0)
def create_teamperson(teamperson: TeamPerson, session: SessionDep = Depends(get_session)):
    """Create a teamperson."""
    return create_teamperson_service(teamperson, session)


@router.get("/read-teampersons/{teamperson_id}")
@version(1, 0)
async def read_teamperson(teamperson_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a teamperson by its ID."""
    return read_teamperson_service(teamperson_id, session)

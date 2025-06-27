from fastapi import APIRouter, Depends
from src.models.person import Person
from src.services.person_service import create_person_service, read_person_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-person/")
@version(1, 0)
def create_person(person: Person, session: SessionDep = Depends(get_session)):
    """Create a person."""
    return create_person_service(person, session)


@router.get("/persons/{person_id}")
@version(1, 0)
async def read_person(person_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a person by their ID."""
    return read_person_service(person_id, session)

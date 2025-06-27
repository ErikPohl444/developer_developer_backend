from fastapi import APIRouter, Depends
from src.models.user import User
from src.services.user_service import create_user_service, read_user_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-user/")
@version(1, 0)
def create_user(user: User, session: SessionDep = Depends(get_session)):
    """Create a user."""
    return create_user_service(user, session)


@router.get("/users/{user_id}")
@version(1, 0)
async def read_user(user_id: int, session: SessionDep = Depends(get_session), q: str = None):
    """Retrieve a user by its ID."""
    return read_user_service(user_id, session)

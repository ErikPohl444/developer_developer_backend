from fastapi import APIRouter, Depends
from src.models.role import Role
from src.services.role_service import create_role_service, read_role_service
from src.main import SessionDep, get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import VersionedFastAPI, version

router = APIRouter()


@router.post("/create-role/")
@version(1, 0)
def create_role(role: Role, session: SessionDep = Depends(get_session)):
    return create_role_service(role, session)


@router.get("/roles/{role_id}")
@version(1, 0)
async def read_role(role_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_role_service(role_id, session)

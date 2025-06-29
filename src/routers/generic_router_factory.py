from fastapi import APIRouter
from fastapi_versioning import version


def create_crud_router(
    model,
    create_service,
    read_service,
    read_all_service,
    resource_name: str,
    session_dep
):
    router = APIRouter()

    @router.post(f"/{resource_name}/")
    @version(1, 0)
    def create_resource(
            item: model,
            session: session_dep
    ):
        """Create a resource."""  # was session_dep =Depends(get_session_func)
        return create_service(item, session)

    @router.get(f"/{resource_name}/{{item_id}}")
    @version(1, 0)
    async def read_resource(item_id: int, session: session_dep, q: str = None):
        """Retrieve a resource by its ID."""
        return read_service(item_id, session)

    @router.get(f"/{resource_name}/")
    @version(1, 0)
    async def read_resource(session: session_dep, q: str = None):
        """Retrieve all resource."""
        return read_all_service(session)

    return router

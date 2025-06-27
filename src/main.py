from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version

# service
from src.services.db_service import create_db_and_tables


# routers
from src.routers.user_router import router as user_router
from src.routers.skill_router import router as skill_router
from src.routers.skilltool_router import router as skilltool_router
from src.routers.team_router import router as team_router
from src.routers.tool_router import router as tool_router
from src.routers.teamperson_router import router as teamperson_router
from src.routers.teamgoal_router import router as teamgoal_router
from src.routers.role_router import router as role_router
from src.routers.person_router import router as person_router
from src.routers.persongoal_router import router as persongoal_router
from src.routers.personskill_router import router as personskill_router
from src.routers.personskillhistory_router import router as personskillhistory_router

base_app = FastAPI(title="Developer Developer")
base_app.include_router(person_router)
base_app.include_router(persongoal_router)
base_app.include_router(personskill_router)
base_app.include_router(personskillhistory_router)
base_app.include_router(role_router)
base_app.include_router(skill_router)
base_app.include_router(skilltool_router)
base_app.include_router(team_router)
base_app.include_router(teamgoal_router)
base_app.include_router(teamperson_router)
base_app.include_router(tool_router)
base_app.include_router(user_router)


@base_app.get("/")
@version(1, 0)
async def root():
    return {"message": "Hello World!  Welcome to Develop!"}


@base_app.get("/health")
@version(1, 0)
async def health_check():
    return {"status": "healthy"}

app = VersionedFastAPI(base_app)


@base_app.on_event("startup")
def on_startup():
    create_db_and_tables()

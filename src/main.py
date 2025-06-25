from fastapi import FastAPI, Depends, HTTPException
from fastapi_versioning import VersionedFastAPI, version
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from src.services.user_service import create_user_service, read_user_service
from src.models.user import User
from src.models.skill import Skill
from src.models.goal import Goal
from src.models.teamgoal import TeamGoal
from src.models.persongoal import PersonGoal
from src.models.tool import Tool
from src.models.skilltool import SkillTool
from src.models.role import Role
from src.models.person import Person
from src.models.personskill import PersonSkill
from src.models.personskillhistory import PersonSkillHistory
from src.models.team import Team
from src.models.teamperson import TeamPerson
from src.services.person_service import create_person_service, read_person_service
from src.services.personskill_service import create_personskill_service, read_personskill_service
from src.services.persongoal_service import create_persongoal_service, read_persongoal_service
from src.services.personskillhistory_service import create_personskillhistory_service, read_personskillhistory_service
from src.services.tool_service import create_tool_service, read_tool_service
from src.services.goal_service import create_goal_service, read_goal_service
from src.services.role_service import create_role_service, read_role_service
from src.services.skill_service import create_skill_service, read_skill_service
from src.services.skilltool_service import create_skilltool_service, read_skilltool_service
from src.services.team_service import create_team_service, read_team_service
from src.services.teamgoal_service import create_teamgoal_service, read_teamgoal_service
from src.services.teamperson_service import create_teamperson_service, read_teamperson_service


data = [User(user_id=1, name="Erik", age=52, email="erikpohl.444@gmail.com")]

sqlite_file_name = "./data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


base_app = FastAPI(title="Developer Developer")


def connect_to_db():  # stub, inspiration
    pass  # place holder


def get_db():  # stub, inspiration
    db = connect_to_db()
    try:
        yield db
    finally:
        db.close()


@base_app.get("/")
@version(1, 0)
async def root():
    return {"message": "Hello World!  Welcome to Develop!"}


@base_app.post("/create-user/")
@version(1, 0)
def create_user(user: User, session: SessionDep = Depends(get_session)):
    return create_user_service(user, session)


@base_app.get("/users/{user_id}")
@version(1, 0)
async def read_user(user_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_user_service(user_id, session)


@base_app.post("/create-skill/")
@version(1, 0)
def create_skill(skill: Skill, session: SessionDep = Depends(get_session)):
    return create_skill_service(skill, session)


@base_app.get("/skills/{skill_id}")
@version(1, 0)
async def read_skill(skill_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_skill_service(skill_id, session)


@base_app.post("/create-team/")
@version(1, 0)
def create_team(team: Team, session: SessionDep = Depends(get_session)):
    return create_team_service(team, session)


@base_app.get("/teams/{team_id}")
@version(1, 0)
async def read_team(team_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_team_service(team_id, session)


@base_app.post("/create-tool/")
@version(1, 0)
def create_tool(tool: Tool, session: SessionDep = Depends(get_session)):
    return create_tool_service(tool, session)


@base_app.get("/tools/{tool_id}")
@version(1, 0)
async def read_tool(tool_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_tool_service(tool_id, session)


@base_app.post("/create-person/")
@version(1, 0)
def create_person(person: Person, session: SessionDep = Depends(get_session)):
    return create_person_service(person, session)


@base_app.get("/persons/{person_id}")
@version(1, 0)
async def read_person(person_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_person_service(person_id, session)


@base_app.post("/create-teamperson/")
@version(1, 0)
def create_teamperson(teamperson: TeamPerson, session: SessionDep = Depends(get_session)):
    return create_teamperson_service(teamperson, session)


@base_app.get("/read-teampersons/{teamperson_id}")
@version(1, 0)
async def read_teamperson(teamperson_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_teamperson_service(teamperson_id, session)


@base_app.post("/create-personskill/")
@version(1, 0)
def create_personskill(personskill: PersonSkill, session: SessionDep = Depends(get_session)):
    return create_personskill_service(personskill, session)


@base_app.get("/personskills/{personskill_id}")
@version(1, 0)
async def read_personskill(personskill_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_personskill_service(personskill_id, session)


@base_app.post("/create-personskillhistory/")
@version(1, 0)
def create_personskillhistory(personskillhistory: PersonSkillHistory, session: SessionDep = Depends(get_session)):
    return create_personskillhistory_service(personskillhistory, session)


@base_app.get("/personskillhistories/{personskillhistory_id}")
@version(1, 0)
async def read_personskillhistories(personskillhistory_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_personskillhistory_service(personskillhistory_id, session)


@base_app.post("/create-role/")
@version(1, 0)
def create_role(role: Role, session: SessionDep = Depends(get_session)):
    return create_role_service(role, session)


@base_app.get("/roles/{role_id}")
@version(1, 0)
async def read_role(role_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_role_service(role_id, session)


@base_app.post("/create-skilltool/")
@version(1, 0)
def create_skilltool(skilltool: SkillTool, session: SessionDep = Depends(get_session)):
    return create_skilltool_service(skilltool, session)


@base_app.get("/skilltools/{skilltool_id}")
@version(1, 0)
async def read_skilltool(skilltool_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_skilltool_service(skilltool_id, session)


@base_app.post("/create-goal/")
@version(1, 0)
def create_goal(goal: Goal, session: SessionDep = Depends(get_session)):
    return create_goal_service(goal, session)


@base_app.get("/goals/{goal_id}")
@version(1, 0)
async def read_goal(goal_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_goal_service(goal_id, session)


@base_app.post("/create-teamgoal/")
@version(1, 0)
def create_teamgoal(teamgoal: TeamGoal, session: SessionDep = Depends(get_session)):
    return create_teamgoal_service(teamgoal, session)


@base_app.get("/teamgoals/{teamgoal_id}")
@version(1, 0)
async def read_teamgoal(teamgoal_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_teamgoal_service(teamgoal_id, session)


@base_app.post("/create-persongoal/")
@version(1, 0)
def create_persongoal(persongoal: PersonGoal, session: SessionDep = Depends(get_session)):
    return create_persongoal_service(persongoal, session)


@base_app.get("/persongoals/{persongoal_id}")
@version(1, 0)
async def read_persongoal(persongoal_id: int, session: SessionDep = Depends(get_session), q: str = None):
    return read_persongoal_service(persongoal_id, session)


@base_app.get("/health")
@version(1, 0)
async def health_check():
    return {"status": "healthy"}

app = VersionedFastAPI(base_app)


@base_app.on_event("startup")
def on_startup():
    create_db_and_tables()

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
from src.services.tool_service import create_tool_service, read_tool_service


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


app = FastAPI(title="Developer Developer")


def connect_to_db():  # stub, inspiration
    pass  # place holder


def get_db():  # stub, inspiration
    db = connect_to_db()
    try:
        yield db
    finally:
        db.close()


@app.post("/create-user/")
@version(1, 0)
def create_user(user: User, session: SessionDep):
    return create_user_service(user, session)


@app.get("/users/{user_id}")
@version(1, 0)
async def read_user(user_id: int, session: SessionDep, q: str = None):
    return read_user_service(user_id, session)


@app.post("/create-skill/")
@version(1, 0)
def create_skill(skill: Skill):
    return {
        "message": f"Skill {skill.name} created successfully!",
        "data": skill
    }


@app.get("/skills/{skill_id}")
@version(1, 0)
async def read_skill(skill_id: int, q: str = None):
    return {"skill_id": skill_id, "q": q}


@app.post("/create-team/")
@version(1, 0)
def create_team(team: Team):
    return {
        "message": f"Team {team.name} created successfully!",
        "data": team
    }


@app.get("/teams/{team_id}")
@version(1, 0)
async def read_team(team_id: int, q: str = None):
    return {"team_id": team_id, "q": q}


@app.post("/create-tool/")
@version(1, 0)
def create_tool(tool: Tool):
    return create_tool_service(tool)


@app.get("/tools/{tool_id}")
@version(1, 0)
async def read_tool(tool_id: int, q: str = None):
    return read_tool_service(tool_id)


@app.post("/create-person/")
@version(1, 0)
def create_person(person: Person):
    return create_person_service(person)


@app.get("/persons/{person_id}")
@version(1, 0)
async def read_person(person_id: int, q: str = None):
    return read_person_service(person_id)


@app.post("/create-teamperson/")
@version(1, 0)
def create_teamperson(teamperson: TeamPerson):
    return {
        "message": f"TeamPerson {teamperson.name} created successfully!",
        "data": teamperson
    }


@app.get("/reampersons/{teamperson_id}")
@version(1, 0)
async def read_teamperson(teamperson_id: int, q: str = None):
    return {"teamperson_id": teamperson_id, "q": q}


@app.post("/create-personskill/")
@version(1, 0)
def create_personskill(personskill: PersonSkill):
    return {
        "message": f"PersonSkill {personskill.name} created successfully!",
        "data": personskill
    }


@app.get("/personskills/{personskill_id}")
@version(1, 0)
async def read_personskill(personskill_id: int, q: str = None):
    return {"personskill_id": personskill_id, "q": q}


@app.post("/create-personskillhistory/")
@version(1, 0)
def create_personskillhistory(personskillhistory: PersonSkillHistory):
    return {
        "message": f"PersonSkill {personskillhistory.name} created successfully!",
        "data": personskillhistory
    }


@app.get("/personskillhistories/{personskillhistory_id}")
@version(1, 0)
async def read_personskillhistories(personskillhistory_id: int, q: str = None):
    return {"personskillhistory_id": personskillhistory_id, "q": q}


@app.post("/create-role/")
@version(1, 0)
def create_role(role: Role):
    return {
        "message": f"Role {role.name} created successfully!",
        "data": role
    }


@app.get("/roles/{role_id}")
@version(1, 0)
async def read_role(role_id: int, q: str = None):
    return {"role_id": role_id, "q": q}


@app.post("/create-person/")
@version(1, 0)
def create_person(person: Role):
    return {
        "message": f"Person {person.name} created successfully!",
        "data": person
    }


@app.get("/people/{person_id}")
@version(1, 0)
async def read_person(person_id: int, q: str = None):
    return {"person_id": person_id, "q": q}


@app.post("/create-tool/")
@version(1, 0)
def create_tool(tool: SkillTool):
    return {
        "message": f"Tool {tool.name} created successfully!",
        "data": tool
    }


@app.get("/tools/{tool_id}")
@version(1, 0)
async def read_tool(tool_id: int, q: str = None):
    return {"tool_id": tool_id, "q": q}


@app.post("/create-goal/")
@version(1, 0)
def create_goal(goal: Goal):
    return {
        "message": f"Goal {goal.name} created successfully!",
        "data": goal
    }


@app.get("/goals/{goal_id}")
@version(1, 0)
async def read_goal(goal_id: int, q: str = None):
    return {"goal_id": goal_id, "q": q}


@app.post("/create-teamgoal/")
@version(1, 0)
def create_teamgoal(teamgoal: TeamGoal):
    return {
        "message": f"TeamGoal {teamgoal.name} created successfully!",
        "data": teamgoal
    }


@app.get("/teamgoals/{teamgoal_id}")
@version(1, 0)
async def read_teamgoal(teamgoal_id: int, q: str = None):
    return {"teamgoal_id": teamgoal_id, "q": q}


@app.post("/create-persongoal/")
@version(1, 0)
def create_persongoal(persongoal: PersonGoal):
    return {
        "message": f"PersonGoal {persongoal.name} created successfully!",
        "data": persongoal
    }


@app.get("/persongoals/{persongoal_id}")
@version(1, 0)
async def read_persongoal(persongoal_id: int, q: str = None):
    return {"persongoal_id": persongoal_id, "q": q}


@app.get("/")
@version(1, 0)
async def root():
    return {"message": "Hello World!  Welcome to Develop!"}


@app.get("/health")
@version(1, 0)
async def health_check():
    return {"status": "healthy"}

app = VersionedFastAPI(app)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

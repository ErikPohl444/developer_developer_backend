import datetime

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version
from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    age: int
    email: str


data = [User(user_id=1, name="Erik", age=52, email="erikpohl.444@gmail.com")]


class Skill(BaseModel):
    skill_id: int
    name: str


class Goal(BaseModel):
    goal_id: int
    skill_id: int
    name: str


class TeamGoal(BaseModel):
    goal_id: int
    team_id: int
    max_team_score_exceeds: int
    avg_score: int
    due_date: datetime.date


class PersonGoal(BaseModel):
    goal_id: int
    person_id: int
    exceeds_score: int
    due_date: datetime.date


class Tool(BaseModel):
    tool_id: int
    tool_name: str


class SkillTool(BaseModel):
    skilltool_id: int
    tool_id: int
    skill_id: int


class Role(BaseModel):
    role_id: int
    name: str


class Person(BaseModel):
    person_id: int
    name: str
    role_id: int


class PersonSkill(BaseModel):
    personskill_id: int
    person_id: int
    skill_id: int
    score: int


class PersonSkillHistory(BaseModel):
    personskill_id: int
    date: datetime.date
    score: int


class Team(BaseModel):
    team_id: int
    parent_team_id: int
    name: str
    manager: int


class TeamPerson(BaseModel):
    teamperson_id: int
    team_id: int
    person_id: int


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
def create_user(user: User):
    data[0] = user
    return {
        "message": f"User {user.name} created successfully!",
        "data": user
    }


@app.get("/users/{user_id}")
@version(1, 0)
async def read_user(user_id: int, q: str = None):
    x = data[0]
    return {"user_id": x.user_id, "user": x, "q": q}


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


@app.get("/teams/{team_id}")
@version(1, 0)
async def read_team(team_id: int, q: str = None):
    return {"team_id": team_id, "q": q}


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


@app.get("/")
@version(1, 0)
async def root():
    return {"message": "Hello World!  Welcome to Develop!"}

@app.get("/health")
@version(1, 0)
async def health_check():
    return {"status": "healthy"}

app = VersionedFastAPI(app)

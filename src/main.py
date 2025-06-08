import datetime

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    name: str
    age: int
    email: str

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

class SkillTool(BaseModel):
    tool_id: int
    skill_id: int
    tool_name: str

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


app = FastAPI()

def connect_to_db(): # stub, inspiration
    pass # place holder
def get_db(): # stub, inspiration
    db = connect_to_db()
    try:
        yield db
    finally:
        db.close()


@app.post("/create-user/")
def create_user(user: User):
    return {
        "message": f"User {user.name} created successfully!",
        "data": user
    }

@app.post("/create-skill/")
def create_skill(skill: Skill):
    return {
        "message": f"Skill {skill.name} created successfully!",
        "data": skill
    }

@app.post("/create-role/")
def create_skill(role: Role):
    return {
        "message": f"Skill {role.name} created successfully!",
        "data": role
    }

@app.post("/create-person/")
def create_skill(person: Role):
    return {
        "message": f"Person {person.name} created successfully!",
        "data": person
    }

@app.post("/create-team/")
def create_skill(team: Team):
    return {
        "message": f"Person {team.name} created successfully!",
        "data": team
    }

@app.post("/create-skilltool/")
def create_skill(skilltool: SkillTool):
    return {
        "message": f"Person {skilltool.name} created successfully!",
        "data": skilltool
    }

@app.post("/create-goal/")
def create_skill(goal: Goal):
    return {
        "message": f"Person {goal.name} created successfully!",
        "data": goal
    }

@app.get("/")
async def root():
    return {"message": "Hello World!  Welcome to Develop!"}

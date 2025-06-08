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


@app.get("/")
async def root():
    return {"message": "Hello World"}
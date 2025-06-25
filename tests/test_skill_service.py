import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.skill import Skill
from src.services.skill_service import (
    create_skill_service,
    read_skill_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_skill_service(in_memory_session):
    skill = Skill(name="Test skill")
    result = create_skill_service(skill, in_memory_session)
    assert result["message"] == f"Skill {skill.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test skill"


def test_read_skill_service_found(in_memory_session):
    skill = Skill(name="Read skill")
    in_memory_session.add(skill)
    in_memory_session.commit()
    in_memory_session.refresh(skill)
    fetched = read_skill_service(skill.id, in_memory_session)
    assert fetched.id == skill.id
    assert fetched.name == "Read skill"


def test_read_skill_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_skill_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "skill not found"

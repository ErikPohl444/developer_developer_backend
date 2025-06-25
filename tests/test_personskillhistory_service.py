import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.personskillhistory import PersonSkillHistory
from src.services.personskillhistory_service import (
    create_personskillhistory_service,
    read_personskillhistory_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_personskillhistory_service(in_memory_session):
    personskillhistory = PersonSkillHistory(name="Test personskillhistory")
    result = create_personskillhistory_service(personskillhistory, in_memory_session)
    assert result["message"] == f"personskillhistory {personskillhistory.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test personskillhistory"


def test_read_personskillhistory_service_found(in_memory_session):
    personskillhistory = PersonSkillHistory(name="Read personskillhistory")
    in_memory_session.add(personskillhistory)
    in_memory_session.commit()
    in_memory_session.refresh(personskillhistory)
    fetched = read_personskillhistory_service(personskillhistory.id, in_memory_session)
    assert fetched.id == personskillhistory.id
    assert fetched.name == "Read personskillhistory"


def test_read_personskillhistory_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_personskillhistory_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "personskillhistory not found"

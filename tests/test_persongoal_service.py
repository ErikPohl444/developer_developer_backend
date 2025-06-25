import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.persongoal import PersonGoal
from src.services.persongoal_service import (
    create_persongoal_service,
    read_persongoal_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_persongoal_service(in_memory_session):
    persongoal = PersonGoal(name="Test Goal")
    result = create_persongoal_service(persongoal, in_memory_session)
    assert result["message"] == f"PersonGoal {persongoal.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test Goal"


def test_read_persongoal_service_found(in_memory_session):
    persongoal = PersonGoal(name="Read Goal")
    in_memory_session.add(persongoal)
    in_memory_session.commit()
    in_memory_session.refresh(persongoal)
    fetched = read_persongoal_service(persongoal.id, in_memory_session)
    assert fetched.id == persongoal.id
    assert fetched.name == "Read Goal"


def test_read_persongoal_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_persongoal_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "PersonGoal not found"

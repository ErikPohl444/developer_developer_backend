import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.teamgoal import TeamGoal
from src.services.teamgoal_service import (
    create_teamgoal_service,
    read_teamgoal_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_teamgoal_service(in_memory_session):
    teamgoal = TeamGoal(name="Test teamgoal")
    result = create_teamgoal_service(teamgoal, in_memory_session)
    assert result["message"] == f"TeamGoal {teamgoal.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test teamgoal"


def test_read_teamgoal_service_found(in_memory_session):
    teamgoal = TeamGoal(name="Read teamgoal")
    in_memory_session.add(teamgoal)
    in_memory_session.commit()
    in_memory_session.refresh(teamgoal)
    fetched = read_teamgoal_service(teamgoal.id, in_memory_session)
    assert fetched.id == teamgoal.id
    assert fetched.name == "Read teamgoal"


def test_read_teamgoal_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_teamgoal_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "teamgoal not found"

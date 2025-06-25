import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.goal import Goal
from src.services.goal_service import (
    create_goal_service,
    read_goal_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_goal_service(in_memory_session):
    goal = Goal(name="Test Goal")
    result = create_goal_service(goal, in_memory_session)
    assert result["message"] == f"Goal {goal.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test Goal"


def test_read_goal_service_found(in_memory_session):
    goal = Goal(name="Read Goal")
    in_memory_session.add(goal)
    in_memory_session.commit()
    in_memory_session.refresh(goal)
    fetched = read_goal_service(goal.id, in_memory_session)
    assert fetched.id == goal.id
    assert fetched.name == "Read Goal"


def test_read_goal_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_goal_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Goal not found"

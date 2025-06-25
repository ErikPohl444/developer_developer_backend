import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.team import Team
from src.services.team_service import (
    create_team_service,
    read_team_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_team_service(in_memory_session):
    team = Team(name="Test team")
    result = create_team_service(team, in_memory_session)
    assert result["message"] == f"Team {team.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test team"


def test_read_team_service_found(in_memory_session):
    team = Team(name="Read team")
    in_memory_session.add(team)
    in_memory_session.commit()
    in_memory_session.refresh(team)
    fetched = read_team_service(team.id, in_memory_session)
    assert fetched.id == team.id
    assert fetched.name == "Read team"


def test_read_team_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_team_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "team not found"

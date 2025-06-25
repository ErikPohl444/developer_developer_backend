import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.teamperson import TeamPerson
from src.services.teamperson_service import (
    create_teamperson_service,
    read_teamperson_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_teamperson_service(in_memory_session):
    teamperson = TeamPerson(name="Test teamperson")
    result = create_teamperson_service(teamperson, in_memory_session)
    assert result["message"] == f"TeamPerson {teamperson.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test teamperson"


def test_read_teamperson_service_found(in_memory_session):
    teamperson = TeamPerson(name="Read teamperson")
    in_memory_session.add(teamperson)
    in_memory_session.commit()
    in_memory_session.refresh(teamperson)
    fetched = read_teamperson_service(teamperson.id, in_memory_session)
    assert fetched.id == teamperson.id
    assert fetched.name == "Read teamperson"


def test_read_teamperson_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_teamperson_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "teamperson not found"

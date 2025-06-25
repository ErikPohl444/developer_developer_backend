import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.personskill import PersonSkill
from src.services.personskill_service import (
    create_personskill_service,
    read_personskill_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_personskill_service(in_memory_session):
    personskill = PersonSkill(name="Test personskill")
    result = create_personskill_service(personskill, in_memory_session)
    assert result["message"] == f"personskill {personskill.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test personskill"


def test_read_personskill_service_found(in_memory_session):
    personskill = PersonSkill(name="Read personskill")
    in_memory_session.add(personskill)
    in_memory_session.commit()
    in_memory_session.refresh(personskill)
    fetched = read_personskill_service(personskill.id, in_memory_session)
    assert fetched.id == personskill.id
    assert fetched.name == "Read personskill"


def test_read_personskill_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_personskill_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "personskill not found"

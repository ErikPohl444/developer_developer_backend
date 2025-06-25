import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.person import Person
from src.services.person_service import (
    create_person_service,
    read_person_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_person_service(in_memory_session):
    person = Person(name="Test Person")
    result = create_person_service(person, in_memory_session)
    assert result["message"] == f"Person {person.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test Person"


def test_read_person_service_found(in_memory_session):
    person = Person(name="Read Person")
    in_memory_session.add(person)
    in_memory_session.commit()
    in_memory_session.refresh(person)
    fetched = read_person_service(person.id, in_memory_session)
    assert fetched.id == person.id
    assert fetched.name == "Read Person"


def test_read_person_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_person_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Person not found"

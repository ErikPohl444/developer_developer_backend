import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.user import User
from src.services.user_service import (
    create_user_service,
    read_user_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_user_service(in_memory_session):
    user = User(name="Test user")
    result = create_user_service(user, in_memory_session)
    assert result["message"] == f"User {user.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test user"


def test_read_user_service_found(in_memory_session):
    user = User(name="Read user")
    in_memory_session.add(user)
    in_memory_session.commit()
    in_memory_session.refresh(user)
    fetched = read_user_service(user.id, in_memory_session)
    assert fetched.id == user.id
    assert fetched.name == "Read user"


def test_read_user_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_user_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "user not found"

import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.role import Role
from src.services.role_service import (
    create_role_service,
    read_role_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_role_service(in_memory_session):
    role = Role(name="Test role")
    result = create_role_service(role, in_memory_session)
    assert result["message"] == f"Role {role.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test role"


def test_read_role_service_found(in_memory_session):
    role = Role(name="Read role")
    in_memory_session.add(role)
    in_memory_session.commit()
    in_memory_session.refresh(role)
    fetched = read_role_service(role.id, in_memory_session)
    assert fetched.id == role.id
    assert fetched.name == "Read role"


def test_read_role_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_role_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "role not found"

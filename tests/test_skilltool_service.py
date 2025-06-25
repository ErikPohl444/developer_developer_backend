import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.skilltool import SkillTool
from src.services.skilltool_service import (
    create_skilltool_service,
    read_skilltool_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_skilltool_service(in_memory_session):
    skilltool = SkillTool(name="Test skilltool")
    result = create_skilltool_service(skilltool, in_memory_session)
    assert result["message"] == f"SkillTool {skilltool.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test skilltool"


def test_read_skilltool_service_found(in_memory_session):
    skilltool = SkillTool(name="Read skilltool")
    in_memory_session.add(skilltool)
    in_memory_session.commit()
    in_memory_session.refresh(skilltool)
    fetched = read_skilltool_service(skilltool.id, in_memory_session)
    assert fetched.id == skilltool.id
    assert fetched.name == "Read skilltool"


def test_read_skilltool_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_skilltool_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "skilltool not found"

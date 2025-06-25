import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from src.models.tool import Tool
from src.services.tool_service import (
    create_tool_service,
    read_tool_service,
)


@pytest.fixture
def in_memory_session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_tool_service(in_memory_session):
    tool = Tool(name="Test tool")
    result = create_tool_service(tool, in_memory_session)
    assert result["message"] == f"Tool {tool.name} created successfully!"
    assert hasattr(result["data"], "id")
    assert result["data"].name == "Test tool"


def test_read_tool_service_found(in_memory_session):
    tool = Tool(name="Read tool")
    in_memory_session.add(tool)
    in_memory_session.commit()
    in_memory_session.refresh(tool)
    fetched = read_tool_service(tool.id, in_memory_session)
    assert fetched.id == tool.id
    assert fetched.name == "Read tool"


def test_read_tool_service_not_found(in_memory_session):
    with pytest.raises(HTTPException) as excinfo:
        read_tool_service(999, in_memory_session)
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "tool not found"

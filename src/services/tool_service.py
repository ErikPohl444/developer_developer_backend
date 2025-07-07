from fastapi import HTTPException
from sqlmodel import Session
from src.models.tool import Tool
from src.services.generic_return_all_items_service import read_all_items_service
from src.services.generic_create_item_service import create_item_service


def create_tool_service(tool: Tool, session: Session):
    return create_item_service(session, tool)


def read_tool_service(tool_id: int, session: Session):
    tool = session.get(Tool, tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool


def read_all_tools_service(session: Session):
    return read_all_items_service(session, Tool)

from fastapi import HTTPException
from sqlmodel import Session
from src.models.tool import Tool

def create_tool_service(tool: Tool, session: Session):
    session.add(tool)
    session.commit()
    session.refresh(tool)
    return {
        "message": f"Tool {tool.name} created successfully!",
        "data": tool
    }

def read_tool_service(tool_id: int, session: Session):
    tool = session.get(Tool, tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="User not found")
    return tool
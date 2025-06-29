from fastapi import HTTPException
from sqlmodel import Session, select
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
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool


def read_all_tools_service(session: Session):
    with session:
        statement = select(Tool)
        tools = session.exec(statement)
        if not tools:
            raise HTTPException(status_code=404, detail="Tools not found")
        all_tools = tools.all()
    return all_tools

from typing import Type, List
from sqlmodel import Session, SQLModel, select
from fastapi import HTTPException


def read_all_items_service(session: Session, Item: Type[SQLModel]) -> List[SQLModel]:
    statement = select(Item)
    results = session.exec(statement)
    all_items = results.all()
    if not all_items:
        raise HTTPException(status_code=404, detail=f"No {Item.__name__}s found")
    return all_items

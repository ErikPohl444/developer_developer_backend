from sqlmodel import Session, SQLModel
from fastapi import HTTPException

def return_one_item_service(item_model: SQLModel, item_id: int, session: Session):
    item = session.get(item_model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"{item_model.__name__} not found")
    return item
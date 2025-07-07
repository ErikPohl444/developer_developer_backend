from typing import Type, List
from sqlmodel import Session, SQLModel


def create_item_service(session: Session, item: Type[SQLModel]) -> List[SQLModel]:
    session.add(item)
    session.commit()
    session.refresh(item)
    return {
        "message": f"{item.__name__} {item.name} created successfully!",
        "data": item
    }

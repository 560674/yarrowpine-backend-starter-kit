from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlalchemy import select

from app.deps import SessionDep
from app.models import Item
from app.schemas import ItemCreate, ItemOut, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])


def _get(db: SessionDep, item_id: int) -> Item:
    item = db.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.get("", response_model=list[ItemOut])
def list_items(db: SessionDep, limit: int = Query(default=20, ge=1, le=100)) -> list[Item]:
    return list(db.scalars(select(Item).order_by(Item.id.desc()).limit(limit)).all())


@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(body: ItemCreate, db: SessionDep) -> Item:
    item = Item(title=body.title, description=body.description)
    db.add(item)
    db.commit()
    return item


@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int, db: SessionDep) -> Item:
    return _get(db, item_id)


@router.patch("/{item_id}", response_model=ItemOut)
def update_item(item_id: int, body: ItemUpdate, db: SessionDep) -> Item:
    item = _get(db, item_id)
    for key, value in body.model_dump(exclude_unset=True).items():
        if value is not None:
            setattr(item, key, value)
    db.commit()
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: SessionDep) -> Response:
    db.delete(_get(db, item_id))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

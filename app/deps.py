from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.orm import Session


def get_db(request: Request):
    yield from request.app.state.db.session()


SessionDep = Annotated[Session, Depends(get_db)]

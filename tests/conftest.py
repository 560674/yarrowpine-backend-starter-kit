import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import Settings
from app.db import Database
from app.main import create_app


@pytest.fixture
def client():
    database = Database("sqlite://")
    database.engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    database.session_factory = sessionmaker(bind=database.engine, expire_on_commit=False)
    with TestClient(create_app(Settings(_env_file=None), database)) as test_client:
        yield test_client

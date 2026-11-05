# Backend Starter Kit

*A minimal backend starter for FastAPI projects — free edition*

FastAPI is a trademark of José Sebastián Ramírez Montaño. Python® is a registered trademark of the Python Software Foundation. Swagger® is a registered trademark of SmartBear Software Inc. Redoc® is a registered trademark of Redocly Inc. Ruff® is a registered trademark of Astral Software Inc. Independent product, not affiliated with, endorsed by, or sponsored by any of them.

A small, tested starting point: an items CRUD API on SQLite with typed settings, Ruff and pytest.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:create_app --factory --reload
ruff check . && pytest
```

Open http://127.0.0.1:8000/docs.

**Free edition:** items CRUD, health check, 3 tests. The Pro edition adds sign-in with access tokens, user roles,
ownership checks, search and pagination, Alembic migrations, secret checks and 19 tests.

Third-party packages are installed from PyPI under their own licences (MIT, BSD, Apache-2.0, PSF); none are bundled.

Built with AI assistance and reviewed by hand.

MIT License. Copyright (c) 2026 Yarrowpine Studio.

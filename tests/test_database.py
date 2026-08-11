from sqlalchemy import text

from app.database.connection import engine
from app.database.dependencies import get_db


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        assert result.scalar() == 1


def test_database_session():
    db_generator = get_db()
    db = next(db_generator)

    try:
        result = db.execute(text("SELECT 1"))

        assert result.scalar() == 1
    finally:
        db.close()
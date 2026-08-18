from sqlalchemy import text

from app.database.connection import SessionLocal, engine
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import create_user, get_user, get_users


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


def test_user_crud():
    db = SessionLocal()
    user = None

    try:
        user_data = UserCreate(
            name="Test User",
            email="testuser@example.com"
        )

        # CREATE
        user = create_user(db, user_data)

        assert user.id is not None
        assert user.name == "Test User"
        assert user.email == "testuser@example.com"

        # GET ONE
        fetched_user = get_user(db, user.id)

        assert fetched_user is not None
        assert fetched_user.id == user.id
        assert fetched_user.email == "testuser@example.com"

        # GET ALL
        users = get_users(db)

        assert len(users) >= 1

    finally:
        if user is not None:
            db.delete(user)
            db.commit()

        db.close()
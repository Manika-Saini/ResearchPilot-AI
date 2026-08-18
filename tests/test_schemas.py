from app.schemas.user import UserCreate, UserResponse


def test_user_create_schema():
    user = UserCreate(
        name="Manika",
        email="manika@example.com"
    )

    assert user.name == "Manika"
    assert user.email == "manika@example.com"


def test_user_response_schema():
    user = UserResponse(
        id=1,
        name="Manika",
        email="manika@example.com"
    )

    assert user.id == 1
    assert user.name == "Manika"
    assert user.email == "manika@example.com"
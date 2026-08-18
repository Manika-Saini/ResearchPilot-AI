


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "API Test User",
            "email": "apitest@example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "API Test User"
    assert data["email"] == "apitest@example.com"
    assert "id" in data


def test_get_user(client):
    # Create user first
    create_response = client.post(
        "/users/",
        json={
            "name": "Get Test User",
            "email": "gettest@example.com"
        }
    )

    assert create_response.status_code == 200

    user_id = create_response.json()["id"]

    # Get user
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["name"] == "Get Test User"
    assert data["email"] == "gettest@example.com"


def test_get_all_users(client):
    response = client.get("/users/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_get_nonexistent_user(client):
    response = client.get("/users/999999")

    assert response.status_code == 404

    assert response.json()["detail"] == "User not found"

def test_invalid_email(client):
    response = client.post(
        "/users/",
        json={
            "name": "Invalid Email",
            "email": "not-an-email"
        }
    )

    assert response.status_code == 422


def test_short_name(client):
    response = client.post(
        "/users/",
        json={
            "name": "A",
            "email": "valid@example.com"
        }
    )

    assert response.status_code == 422


def test_duplicate_email(client):
    email = "duplicate@example.com"

    first_response = client.post(
        "/users/",
        json={
            "name": "First User",
            "email": email
        }
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/users/",
        json={
            "name": "Second User",
            "email": email
        }
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email already registered"
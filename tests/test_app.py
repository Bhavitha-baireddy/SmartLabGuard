from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_valid_submission():
    client = app.test_client()

    code = """
def add(a, b):
    return a + b
"""

    response = client.post(
        "/validate",
        data={"code": code}
    )

    assert response.status_code == 200
    assert b"PASSED" in response.data


def test_invalid_python():
    client = app.test_client()

    code = """
def add(a, b)
    return a + b
"""

    response = client.post(
        "/validate",
        data={"code": code}
    )

    assert response.status_code == 200
    assert b"FAILED" in response.data
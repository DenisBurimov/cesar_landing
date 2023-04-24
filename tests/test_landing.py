import pytest
from flask.testing import FlaskClient
from app import db, create_app
from app.models import User, Contact


@pytest.fixture
def client():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
        app_ctx.pop()


def test_route(client: FlaskClient):
    response = client.get("/")

    assert response.status_code == 200
    assert b"real neighbourhood offer" in response.data
    assert b"trusted homebuyer" in response.data


def test_users_save(client: FlaskClient):
    users_count = User.query.count()

    User(
        username="User_01",
        password="pass"
    ).save()

    assert User.query.count() == users_count + 1


def test_contact_save(client: FlaskClient):
    TESTING_ADDRESS = "Simple2B"
    TESTING_PHONE = "+380555555555"

    contacts_count = Contact.query.count()
    response = client.post(
        "/",
        data=dict(
            address=TESTING_ADDRESS,
            phone=TESTING_PHONE,
        ),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert Contact.query.count() == contacts_count + 1

import pytest
from app import create_app
from app.models.user import User
from app.models.transaction import Transaction
from app.models.stock import Stock
from app import db

@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING":True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# This fixture creates a user and saves it in the database
# @pytest.fixture
# def one_user(app):
#     new_user = User(
#         user_id=1,
#         username="user1",
#         password="user1pw",
#         is_logged_in=False
#     )
#     db.session.add(new_user)
#     db.session.commit()
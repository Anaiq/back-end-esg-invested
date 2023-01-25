from werkzeug.exceptions import HTTPException
# from app.routes import validate_model
from app.models.user import User
from app.models.transaction import Transaction
from app.models.stock import Stock
import pytest


def test_get_all_users_no_saved_users(client):
    ...


def test_get_all_users_one_saved_users(client, one_user):
    ...

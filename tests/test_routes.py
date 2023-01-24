from werkzeug.exceptions import HTTPException
# from app.routes import validate_model
# from app.models.model import Model
import pytest


def test_get_all_users_no_saved_users(client):
    ...


def test_get_all_users_one_saved_users(client, one_user):
    ...

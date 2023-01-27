from werkzeug.exceptions import HTTPException
# from app.routes import validate_model
from app.models.investor import Investor
from app.models.transaction import Transaction
from app.models.stock import Stock
import pytest


def test_get_all_investors_no_saved_investors(client):
    ...


def test_get_all_investors_one_saved_investors(client, one_investor):
    ...

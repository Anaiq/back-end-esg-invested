from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.investor import Investor
from app.models.transaction import Transaction
from app.models.stock import Stock
from app.models.exchange import Exchange
from app.exchange_routes import validate_model
import os, requests

# create  blueprint here
transaction_bp = Blueprint("transaction_bp", __name__, url_prefix="/transactions")



# send a request to delete a transaction from a particular investor's in the database
@transaction_bp.route("/<transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    transaction = validate_model(Transaction, transaction_id)

    db.session.delete(transaction)
    db.session.commit()

    return {"details": f'{transaction.company_name} successfully sold)'}
    
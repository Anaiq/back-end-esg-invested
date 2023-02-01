from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.investor import Investor
from app.models.transaction import Transaction
from app.models.stock import Stock
from app.models.exchange import Exchange
from app.exchange_routes import validate_model
import os, requests

# create blueprint here
investor_bp = Blueprint("investor_bp", __name__, url_prefix="/investors")
transaction_bp = Blueprint("transaction_bp", __name__, url_prefix="/transactions")
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")

# register page: 
    # check if investor in db if not, add investor to db
    # CREATE INVESTOR/POST
@investor_bp.route("", methods=["POST"])
def register_investor():
    # get response for potentially added new investor
    request_body = request.get_json()

    if "investor_name" not in request_body:
        return make_response({"Details": "User name and password required"}, 400)
    
    # get all investors
    investors = Investor.query.all()
    print("investors: ", investors)

    # check if investor in db:
    for investor in investors:
        if request_body["investor_name"]== investor.to_dict()["investor_name"]:
            # if investor in database already:
            return make_response({"Details": "User name and password already taken."}, 400)
    
    # if not add investor to db
    request_body = request.get_json()
    new_investor = Investor.from_dict(request_body)

    db.session.add(new_investor)
    db.session.commit()
    response_body = new_investor.to_dict()

    return make_response(response_body, 201)

# login page: 
    # get one investor

# portfolio page:
    # 



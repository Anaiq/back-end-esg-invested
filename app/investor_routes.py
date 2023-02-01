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
    print("request body:", request_body)

    if "investor_name" not in request_body:
        return make_response({"Details": "User name and password required"}, 400)
    
    # get all investors
    investors = Investor.query.all()
    print("investors: ", investors)

    for investor in investors:
        # check if investor in db:
        if request_body["investor_name"]== investor.to_dict()["investor_name"]:
            # if investor in database already:
            return make_response({"Details": "User name and password already taken."}, 409)
    
    # if not add investor to db
    request_body = request.get_json()
    new_investor = Investor.from_dict(request_body)

    db.session.add(new_investor)
    db.session.commit()
    response_body = new_investor.to_dict()

    return make_response(response_body, 201)


    # GET ONE INVESTOR
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_one_investor_login(investor_id):
    # get all investors
    investors = Investor.query.all()

    investor_to_login = validate_model(Investor, investor_id)

    investor_to_login = investor_to_login.to_dict()
    
    for investor in investors:
        # check if investor in db:
            if investor_to_login["investor_id"] == investor.to_dict()["investor_id"]:
                return investor_to_login

    return make_response({"Details": "Sorry Username does not have an Investing Account. Please Register for one"}, 400)


# portfolio page:
    # 



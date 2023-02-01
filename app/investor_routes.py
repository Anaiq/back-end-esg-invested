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
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")
esg_goal_bp = Blueprint("esg_goal_bp", __name__, url_prefix="/esg-goals")
current_esg_bp = Blueprint("current_esg_bp", __name__, url_prefix="/current-esgs")
cash_balance_bp = Blueprint("cash_balance_bp", __name__, url_prefix="/cash-balance")
total_assets_bp = Blueprint("total_assets_bp", __name__, url_prefix="/total-assets")
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")
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

    # GET INVESTOR ESG GOALS
    # GET INVESTOR CURRENT ESG RATINGS
    # GET/READ INVESTOR CASH BALANCE
    # GET/READ INVESTOR TOTAL CASH VALUE 
    # GET/READ INVESTOR TOTAL ASSETS BALANCE
    # GET/READ INVESTOR LIST OF TRANSACTIONS TO VIEW IN TABLE
    # GET/READ INVESTOR LIST OF FILTERED TRANSACTIONS
    # POST/ ADD A TRANSACTION TO INVESTORS LIST OF TRANSACTIONS
    # PATCH/UPDATE ADD MONEY TO INVESTOR CASH BALANCE
    # PATCH/UPDATE INVESTOR TOTAL ASSETS BALANCE
    # PATCH/UPDATE INVESTOR TOTAL SHARES CASH VALUE
    # PATCH/UPDATE INVESTOR ESG GOALS
    # PATCH/UPDATE INVESTOR CURRENT ESG RATINGS

    




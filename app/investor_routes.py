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
@investor_bp.route("/<investor_id>/esg-goals", methods=["GET"])
def get_investor_esg_goals(investor_id):
    investor = validate_model(Investor, investor_id)

    return make_response({
        "e_goal": investor.to_dict()["e_goal"],
        "s_goal": investor.to_dict()["s_goal"],
        "g_goal": investor.to_dict()["g_goal"],
    }, 200)



# GET INVESTOR CURRENT ESG RATINGS
@investor_bp.route("/<investor_id>/current-esgs", methods=["GET"])
def get_investor_current_esgs(investor_id):
    investor = validate_model(Investor, investor_id)

    return {
        "current_e_rating": investor.to_dict()["current_e_rating"],
        "current_s_rating": investor.to_dict()["current_s_rating"],
        "current_g_rating": investor.to_dict()["current_g_rating"],
    }, 200

    
# GET/READ INVESTOR CASH BALANCE
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_investor_cash_balance():
    ...
# GET/READ INVESTOR TOTAL CASH VALUE OF SHARES
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_investor_total_shares_cash_value():
    ...
# GET/READ INVESTOR TOTAL ASSETS BALANCE
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_investor_total_assets_balance():
    ...

# GET/READ INVESTOR LIST OF TRANSACTIONS TO VIEW IN TABLE
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_investor_transactions():

    ...
# POST/ ADD A TRANSACTION TO INVESTORS LIST OF TRANSACTIONS
@investor_bp.route("/<investor_id>/transactions", methods=["POST"])
def create_transaction_associated_with_investor(investor_id):
    investor = validate_model(Investor, investor_id)
    stocks = Stock.query.all()


    stock_id = 0

    request_body = request.get_json()
    for stock in stocks:
        if stock.to_dict()["stock_symbol"] == request_body["stock_symbol"]:
            stock_id = stock.to_dict()["stock_id"]
        print(stock.to_dict())
    print(request_body)

    new_transaction = Transaction(
        stock_id=stock_id,
        investor_id=investor_id,
        stock_symbol=request_body["stock_symbol"],
        company_name=request_body["company_name"],
        current_stock_price=request_body["current_stock_price"],
        number_stock_shares=request_body["number_stock_shares"],
        transaction_total_value=request_body["transaction_total_value"],
        transaction_type=request_body["transaction_type"],
        transaction_time=request_body["transaction_time"]
        )
    
    db.session.add(new_transaction)
    db.session.commit()

    return new_transaction.to_dict(), 201


# PATCH/UPDATE ADD MONEY TO INVESTOR CASH BALANCE
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_cash_balance():
    ...

# PATCH/UPDATE INVESTOR TOTAL ASSETS BALANCE
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_total_assets_balance():
    ...
# PATCH/UPDATE INVESTOR TOTAL SHARES CASH VALUE
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_total_shares_cash_value():
    ...
# PATCH/UPDATE INVESTOR ESG GOALS
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_esg_goals():
    ...
# PATCH/UPDATE INVESTOR CURRENT ESG RATINGS
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_current_esgs():
    ...
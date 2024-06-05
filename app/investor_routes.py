from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.investor import Investor
from app.models.transaction import Transaction
from app.models.stock import Stock
from app.models.exchange import Exchange
from app.exchange_routes import validate_model
import os
import requests
import datetime
from flask_cors import cross_origin

# create blueprint here
register_bp = Blueprint("register_bp", __name__, url_prefix="/register")
login_bp = Blueprint("login_bp", __name__, url_prefix="/login")
investor_bp = Blueprint("investor_bp", __name__, url_prefix="/investors")


# register page:
# check if investor in db if not, add investor to db
# CREATE INVESTOR/POST
@register_bp.route("", methods=["POST"])
def register_investor():
    # get request_body of potentially added new investor
    request_body = request.get_json()
    print("request body:", request_body)

    if "investor_name" not in request_body:
        return make_response({"Details": "User name and password required"}, 400)

    # get all investors
    investors = Investor.query.all()
    print("investors: ", investors)

    for investor in investors:
        # check if investor in db:
        if request_body["investor_name"] == investor.to_dict()["investor_name"]:
            # if investor in database already:
            return make_response({"Details": "User name and password already taken."}, 409)

    # if not investor in db
    request_body = request.get_json()
    new_investor = Investor.from_dict(request_body)

    db.session.add(new_investor)
    db.session.commit()
    response_body = new_investor.to_dict()

    return make_response(response_body, 201)

# create a login endpoint, check if in database and return
@login_bp.route("", methods=["POST"])
def login_investor():
    # get response for potentially added new investor
    request_body = request.get_json()
    print("request body:", request_body)

    investors = Investor.query.all()


    # investor = Investor.query(request_body)
    for investor in investors:
        # check if investor in db:
        if request_body["investor_name"] == investor.to_dict()["investor_name"]:
            print(
                f"request_body['investor_name'] {request_body['investor_name']} == investor.to_dict()['investor_name'] {investor.to_dict()['investor_name']}")
            response_body = investor.to_dict()
            print(f"response_body: {response_body}")
            return make_response(response_body, 200)

    return make_response({"Details": "Sorry Username does not have an Investing Account. Please Register for one"}, 400)


# GET all investors()
@investor_bp.route("", methods=["GET"])
def get_all_investor_portfolios():
    # get all investors
    investors = Investor.query.all()

    response = []
    for investor in investors:
        response.append(investor.to_dict())
    return jsonify(response), 200
    # return response.to_dict()


# GET SPECIFIED INVESTOR
@investor_bp.route("/<investor_id>", methods=["GET"])
def get_one_investor_portfolio(investor_id):
    # get all investors
    investors = Investor.query.all()

    investor = validate_model(Investor, investor_id)

    one_investor = investor.to_dict()

    for investor in investors:
        # check if investor in db:
        if one_investor["investor_id"] == investor.to_dict()["investor_id"]:
            return investor.to_dict()

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


# GET/READ INVESTOR LIST OF TRANSACTIONS TO VIEW IN TABLE
@investor_bp.route("/<investor_id>/transactions", methods=["GET"])
def get_investor_transactions(investor_id):
    investor = validate_model(Investor, investor_id)

    transactions_response = []
    for transaction in investor.transactions:
        transactions_response.append(transaction.to_dict())
    return jsonify(transactions_response)


# POST/ ADD A BUY TRANSACTION TO INVESTORS LIST OF TRANSACTIONS
@investor_bp.route("/<investor_id>/buy", methods=["POST"])
def create_buy_transaction_associated_with_investor(investor_id):
    investor = validate_model(Investor, investor_id)
    stocks = Stock.query.all()
    exchanges = Exchange.query.all()

    stock_id = 0

    request_body = request.get_json()

    for stock in stocks:
        if stock.to_dict()["stock_symbol"] == request_body["stock_symbol"]:
            stock_id = stock.to_dict()["stock_id"]
    print(request_body)

    for exchange in exchanges:
        if exchange.to_dict()["stock_symbol"] == request_body["stock_symbol"]:
            company_name = exchange.to_dict()["company_name"]

    new_transaction = Transaction(
        stock_id=stock_id,
        investor_id=investor_id,
        stock_symbol=request_body["stock_symbol"],
        company_name=company_name,
        current_stock_price=round(
            float(request_body["current_stock_price"]) * 100),
        number_stock_shares=request_body["number_stock_shares"],
        transaction_total_value=int(request_body["number_stock_shares"]) * round(
            float(request_body["current_stock_price"]) * 100),
        transaction_type=request_body["transaction_type"],
        transaction_time=datetime.datetime.now()
    )

    investor.cash_balance -= new_transaction.transaction_total_value
    investor.total_shares_cash_value += new_transaction.transaction_total_value
    investor.total_assets_balance = investor.cash_balance + \
        investor.total_shares_cash_value

    db.session.add(new_transaction)
    db.session.commit()

    response_body = investor.to_dict()

    return make_response(response_body, 201)


# POST/ ADD A SELL TRANSACTION TO INVESTORS LIST OF TRANSACTIONS
@investor_bp.route("/<investor_id>/sell", methods=["POST"])
def create_sell_transaction_associated_with_investor(investor_id):
    investor = validate_model(Investor, investor_id)
    stocks = Stock.query.all()
    exchanges = Exchange.query.all()

    stock_id = 0

    request_body = request.get_json()

    for stock in stocks:
        if stock.to_dict()["stock_symbol"] == request_body["stock_symbol"]:
            stock_id = stock.to_dict()["stock_id"]
    print(request_body)

    for exchange in exchanges:
        if exchange.to_dict()["stock_symbol"] == request_body["stock_symbol"]:
            company_name = exchange.to_dict()["company_name"]

    new_transaction = Transaction(
        stock_id=stock_id,
        investor_id=investor_id,
        stock_symbol=request_body["stock_symbol"],
        company_name=company_name,
        current_stock_price=round(
            float(request_body["current_stock_price"]) * 100),
        number_stock_shares=request_body["number_stock_shares"],
        transaction_total_value=int(request_body["number_stock_shares"]) * round(
            float(request_body["current_stock_price"]) * 100),
        transaction_type=request_body["transaction_type"],
        transaction_time=datetime.datetime.now()
    )

    investor.cash_balance += new_transaction.transaction_total_value
    investor.total_shares_cash_value -= new_transaction.transaction_total_value
    investor.total_assets_balance = investor.cash_balance + \
        investor.total_shares_cash_value

    db.session.add(new_transaction)
    db.session.commit()

    response_body = investor.to_dict()

    return make_response(response_body, 201)


# PATCH/UPDATE ADD MONEY TO INVESTOR CASH BALANCE
@investor_bp.route("/<investor_id>/add_money", methods=["PATCH"])
def update_investor_cash_balance(investor_id):
    investor = validate_model(Investor, investor_id)

    request_body = request.get_json()

    investor.cash_balance += request_body["cash"]
    investor.total_assets_balance = investor.cash_balance + \
        investor.total_shares_cash_value

    db.session.commit()
    response_body = investor.to_dict()

    return make_response(response_body, 200)


# PATCH/UPDATE INVESTOR ESG GOALS
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_esg_goals():
    ...

    
# PATCH/UPDATE INVESTOR CURRENT ESG RATINGS
@investor_bp.route("/<investor_id>", methods=["PATCH"])
def update_investor_current_esgs():
    ...

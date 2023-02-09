from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.stock import Stock
import os, requests


# create Blueprint here:
stock_bp = Blueprint("stock_bp", __name__, url_prefix="/stocks")

#VALIDATE MODEL
def validate_model(class_obj,id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{id} is an invalid id"}, 400))
    query_result = class_obj.query.get(id)
    if not query_result:
        abort(make_response({"message":f"Sorry, Not found"}, 404))

    return query_result


# READ ALL  STOCKS RATINGS/ GET
@stock_bp.route("", methods=["GET"])
def read_all_stock_stocks():
    stocks = Stock.query.all()
    
    stocks_response = []

    for stock in stocks:
        stocks_response.append(stock.to_dict())
    return jsonify(stocks_response), 200

# READ ONE stock STOCK/ GET
@stock_bp.route("<stock_id>", methods=["GET"])
def read_one_stock_stock(stock_id):
    stock = validate_model(Stock, stock_id)
    
    return stock.to_dict()
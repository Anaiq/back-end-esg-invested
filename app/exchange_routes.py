from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.exchange import Exchange
import os, requests

# create blueprint here
exchange_bp = Blueprint("exchange_bp", __name__, url_prefix="/exchanges")


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


# routes go here
# READ ALL EXCHANGE STOCKS/ GET
@exchange_bp.route("", methods=["GET"])
def read_all_exchange_stocks():
    exchanges = Exchange.query.all()
    
    exchanges_response = []

    for exchange in exchanges:
        exchanges_response.append(exchange.to_dict())
    return jsonify(exchanges_response), 200

# READ ONE EXCHANGE STOCK/ GET
@exchange_bp.route("<exchange_id>", methods=["GET"])
def read_one_exchange_stock(exchange_id):
    exchange = validate_model(Exchange, exchange_id)
    
    return exchange.to_dict()
from app import db

class Transaction(db.Model):
    # transaction_id
    # stock_symbol
    # stock_name
    # current_stock_price
    # number_stock_shares
    # transaction_total_value
    # transaction_type
    # transaction_time
    # user_id (FOREIGNKEY, REFERENCES
    #     users.user.id)
    # stock_id(FOREIGN_KEY, REFERENCES
    #     stocks.stock_id)
    ...
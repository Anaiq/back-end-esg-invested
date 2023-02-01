from app import db

# one to MANY relationship with Investor and Stock
class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    stock_symbol = db.Column(db.String)
    company_name = db.Column(db.String)
    current_stock_price = db.Column(db.Integer)
    number_stock_shares = db.Column(db.Integer)
    transaction_total_value = db.Column(db.Integer)
    transaction_type = db.Column(db.String)
    transaction_time = db.Column(db.DateTime)
    investor_id = db.Column(db.Integer, db.ForeignKey("investor.investor_id"))
    investor = db.relationship("Investor", back_populates="transactions")
    stock_id = db.Column(db.Integer, db.ForeignKey("stock.stock_id"))
    stock = db.relationship("Stock", back_populates="transactions")

    def to_dict(self):
        transaction_as_dict = {}
        transaction_as_dict["transaction_id"] = self.transaction_id
        transaction_as_dict["stock_symbol"] = self.stock_symbol
        transaction_as_dict["company_name"] = self.company_name
        transaction_as_dict["current_stock_price"] = str(self.current_stock_price)
        transaction_as_dict["number_stock_shares"] = self.number_stock_shares
        transaction_as_dict["transaction_total_value"] = str(self.transaction_total_value)
        transaction_as_dict["transaction_type"] = self.transaction_type
        transaction_as_dict["transaction_time"] = self.transaction_time

        return transaction_as_dict


    @classmethod
    def from_dict(cls, request_body):
        return Transaction(
            transaction_id=request_body["transaction_id"],
            stock_symbol=request_body["stock_symbol"],
            company_name=request_body["company_name"],
            current_stock_price=request_body["current_stock_price"],
            number_stock_shares=request_body["number_stock_shares"],
            transaction_total_value=request_body["transaction_total_value"],
            transaction_type=request_body["transaction_type"],
            transaction_time=request_body["transaction_time"]
        )
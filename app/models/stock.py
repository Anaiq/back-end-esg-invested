from app import db


# ONE to many relationship with Transaction
class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    stock_symbol = db.Column(db.String)
    environment_rating = db.Column(db.String)
    social_rating = db.Column(db.String)
    governance_rating = db.Column(db.String)
    transactions = db.relationship("Transaction", back_populates="stock", lazy=True)


    def to_dict(self):
        transactions_list = []
        for transaction in self.transactions:
            transactions_list.append(transaction.to_dict())

        return {
            "stock_id": self.stock_id,
            "stock_symbol": self.stock_symbol,
            "environment_rating": self.environment_rating,
            "social_rating": self.social_rating,
            "governance_rating": self.governance_rating,
            "transactions": transactions_list
        }

        
    @classmethod
    def from_dict(cls, request_body):
        return Stock(
            stock_symbol=request_body["stock_symbol"],
            environment_rating=request_body["environment_rating"],
            social_rating=request_body["social_rating"],
            governance_rating=request_body["governance_rating"],
        )
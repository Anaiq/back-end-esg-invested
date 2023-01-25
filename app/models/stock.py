from app import db


# ONE to many relationship with Transaction
class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    stock_symbol = db.Column(db.String)
    environment_score = db.Column(db.String)
    social_score = db.Column(db.String)
    government_score = db.Column(db.String)
    transactions = db.relationship("Transaction", back_populates="stock", lazy=True)


    def to_dict(self):
        transactions_list = []
        for transaction in self.transactions:
            transactions_list.append(transaction.to_dict())

        return {
            "stock_id": self.stock_id,
            "stock_symbol": self.stock_symbol,
            "environment_score": self.environment_score,
            "social_score": self.social_score,
            "government_score": self.government_score,
            "transactions": transactions_list
        }

        
    @classmethod
    def from_dict(cls, request_body):
        return Stock(
            stock_id=request_body["stock_id"],
            stock_symbol=request_body["stock_symbol"],
            environment_score=request_body["environment_score"],
            social_score=request_body["social_score"],
            government_score=request_body["government_score"],
        )
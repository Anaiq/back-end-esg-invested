from app import db


class Exchange(db.Model):
    exchange_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String)
    company_name = db.Column(db.String)
    current_stock_price = db.Column(db.Numeric) 
    environment_rating = db.Column(db.String)
    social_rating = db.Column(db.String)
    governance_rating = db.Column(db.String)

    def to_dict(self):
        return {
            "exchange_id": self.exchange_id,
            "stock_symbol": self.stock_symbol,
            "company_name": self.company_name,
            "current_stock_price": str(self.current_stock_price),
            "environment_rating": self.environment_rating,
            "social_rating": self.social_rating,
            "governance_rating": self.governance_rating,
        }

    #function not needed?? confirm
    def from_dict(cls, request_body):
        return Exchange(
            stock_symbol=request_body["stock_symbol"],
            company_name=request_body["company_name"],
            current_stock_price=request_body["current_stock_price"],
            environment_rating=request_body["environment_rating"],
            social_rating=request_body["social_rating"],
            governance_rating=request_body["governance_rating"]
        )

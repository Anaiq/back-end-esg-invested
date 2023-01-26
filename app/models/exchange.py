from app import db


class Exchange(db.Model):
    exchange_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String)
    company_name = db.Column(db.String)
    current_stock_price = db.Column(db.Numeric)
    environment_score = db.Column(db.String)
    social_score = db.Column(db.String)
    governance_score = db.Column(db.String)

def to_dict(self):
    return {
        "exchange_id": self.exchange_id,
        "company_name": self.company_name,
        "stock_symbol": self.stock_symbol,
        "current_price": self.current_price,
        "environment_score": self.environment_score,
        "social_score": self.social_score,
        "governance_score": self.governance_score,
    }

def from_dict(cls, request_body):
    return Exchange(
        exchange_id=request_body["exchange_id"],
        stock_symbol=request_body["stock_symbol"],
        company_name=request_body["company_name"],
        current_stock_price=request_body["current_stock_price"],
        environment_score=request_body["environment_score"],
        social_score=request_body["social_score"],
        governance_score=request_body["governance_score"]
    )

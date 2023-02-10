from app import db

# ONE to many relationship with Transaction
class Investor(db.Model):
    investor_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    investor_name = db.Column(db.String, nullable=False)
    cash_balance = db.Column(db.Integer,nullable=False, server_default=db.text("0"))
    total_shares_buys = db.Column(db.Integer,nullable=False, server_default=db.text("0"))
    total_shares_sales = db.Column(db.Integer,nullable=False, server_default=db.text("0"))
    total_shares_cash_value = db.Column(db.Integer,nullable=False, server_default=db.text("0"))
    total_assets_balance = db.Column(db.Integer,nullable=False, server_default=db.text("0"))
    current_e_rating = db.Column(db.String, nullable=False, server_default="")
    current_s_rating = db.Column(db.String,nullable=False, server_default="")
    current_g_rating = db.Column(db.String,nullable=False, server_default="")
    e_goal = db.Column(db.String,nullable=False, server_default="")
    s_goal = db.Column(db.String,nullable=False, server_default="")
    g_goal = db.Column(db.String,nullable=False, server_default="")
    transactions = db.relationship("Transaction", back_populates="investor", lazy=True)


    def to_dict(self):
        transactions_list = []
        for transaction in self.transactions:
            transactions_list.append(transaction.to_dict())

        return {
            "investor_id": self.investor_id,
            "investor_name": self.investor_name,
            "cash_balance": self.cash_balance,
            "total_shares_buys": self.total_shares_buys,
            "total_shares_sales": self.total_shares_sales,
            "total_shares_cash_value": self.total_shares_cash_value,
            "total_assets_balance": self.total_assets_balance,
            "current_e_rating": self.current_e_rating,
            "current_s_rating": self.current_s_rating,
            "current_g_rating": self.current_g_rating,
            "e_goal": self.e_goal,
            "s_goal": self.s_goal,
            "g_goal": self.g_goal,
            "transactions": transactions_list
        }

    @classmethod
    def from_dict(cls, request_body):
        return Investor(
            investor_name=request_body["investor_name"],
            cash_balance=request_body["cash_balance"],
            total_shares_buys=request_body["total_shares_buys"],
            total_shares_sales=request_body["total_shares_sales"],
            total_shares_cash_value=request_body["total_shares_cash_value"],
            total_assets_balance=request_body["total_assets_balance"],
            current_e_rating=request_body["current_e_rating"],
            current_s_rating=request_body["current_s_rating"],
            current_g_rating=request_body["current_g_rating"],
            e_goal=request_body["e_goal"],
            s_goal=request_body["s_goal"],
            g_goal=request_body["g_goal"],
        )

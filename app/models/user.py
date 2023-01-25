from app import db

# ONE to many relationship with Transaction
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    is_logged_in = db.Column(db.Boolean)
    cash_balance = db.Column(db.Numeric)
    total_shares_buys = db.Column(db.Integer)
    total_shares_sales = db.Column(db.Integer)
    total_shares_cash_value = db.Column(db.Numeric)
    total_assets_balance = db.Column(db.Numeric)
    current_e_score = db.Column(db.String)
    current_s_score = db.Column(db.String)
    current_g_score = db.Column(db.String)
    e_goal = db.Column(db.String)
    s_goal = db.Column(db.String)
    g_goal = db.Column(db.String)
    transactions = db.relationship("Transaction", back_populates="user", lazy=True)


    def to_dict(self):
        transactions_list = []
        for transaction in self.transactions:
            transactions_list.append(transaction.to_dict())

        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "password": self.password,
            "is_logged_in": self.is_logged_in,
            "cash_balance": self.cash_balance,
            "total_shares_buys": self.total_shares_buys,
            "total_shares_sales": self.total_shares_sales,
            "total_shares_cash_value": self.total_shares_cash_value,
            "total_assets_balance": self.total_assets_balance,
            "current_e_score": self.current_e_score,
            "current_s_score": self.current_s_score,
            "current_g_score": self.current_g_score,
            "e_goal": self.e_goal,
            "s_goal": self.s_goal,
            "g_goal": self.g_goal,
            "transactions": transactions_list
        }


    @classmethod
    def from_dict(cls, request_body):
        return User(
            user_id=request_body["user_id"],
            user_name=request_body["user_name"],
            password=request_body["password"],
            is_logged_in=request_body["is_logged_in"],
            cash_balance=request_body["cash_balance"],
            total_shares_buys=request_body["total_shares_buys"],
            total_shares_sales=request_body["total_shares_sales"],
            total_shares_cash_value=request_body["total_shares_cash_value"],
            total_assets_balance=request_body["total_assets_balance"],
            current_e_score=request_body["current_e_score"],
            current_s_score=request_body["current_s_score"],
            current_g_score=request_body["current_g_score"],
            e_goal=request_body["e_goal"],
            s_goal=request_body["s_goal"],
            g_goal=request_body["g_goal"],
        )

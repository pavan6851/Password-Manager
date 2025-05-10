from app import db

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Password {self.service}>"

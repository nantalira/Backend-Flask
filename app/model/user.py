from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    level = db.Column(db.BigInteger(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    
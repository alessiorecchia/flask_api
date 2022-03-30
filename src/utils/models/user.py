from enum import unique
import uuid
from utils.db import db

class User(db.Model):
    user_id = db.Column(db.String(32), primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.String(255), nullable=False, default=db.func.now())

    def to_json(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': str(self.created_at)
        }
from dataclasses import dataclass

from app.configs.database import db
from app.exceptions import InvalidEmailError
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class UserModel(db.Model):

    name: str
    last_name: str
    email: str

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False, unique=True)
    last_name = Column(String(511), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(511), nullable=False)
    # api_key = Column(String(511), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email or not email.endswith('.com'):
            raise InvalidEmailError

        return email.lower()

    @property
    def password(self):
        raise AttributeError('Password cannot be accessed!')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

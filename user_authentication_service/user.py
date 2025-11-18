#!/usr/bin/env python3
""" User model for authentication service """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User class for authentication service """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(255), nullable=False, unique=True)
    hashed_password: str = Column(String(255), nullable=False)
    session_id: str = Column(String(255), nullable=True)
    reset_token: str = Column(String(255), nullable=True)

    def __repr__(self):
        return "<User(id='{}', email='{}')>".format(self.id, self.email)

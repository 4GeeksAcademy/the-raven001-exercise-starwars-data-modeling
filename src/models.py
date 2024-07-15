import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum as SqlEnum
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er
from enum import Enum as PyEnum

Base = declarative_base()

class UserRole(PyEnum):
    ADMIN = 'admin'
    USER = 'user'

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    is_banned = Column(Boolean, default=False)
    role = Column(SqlEnum(UserRole), default=UserRole.USER, nullable=False)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    image_url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    image_url = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character = relationship(Character)
    planet = relationship(Planet)
    user = relationship(User)

## Draw from SQLAlchemy base
try:
    render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except:
    print("There was a problem genering the diagram")
    raise Exception
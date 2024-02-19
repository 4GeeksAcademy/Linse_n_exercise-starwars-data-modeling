import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(230), nullable=False)
    name = Column(String(250), nullable=False)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(10))
    eye_color = Column(String(20))
    hair_color = Column(String(15))
    height = Column(Integer)
    skin_color = Column(String(15))
    mass = Column(Integer)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = (Integer)
    diameter = Column(Integer)
    gravity = Column(String(20))
    orbital_period = Column(Integer)
    rotation_period = Column(String(15))
    population = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    minimun_crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    
class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table favorite.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

#!/usr/bin/python3
"""Defines the State class linked to the states table."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state stored in the states table."""

    __tablename__ = "states"
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

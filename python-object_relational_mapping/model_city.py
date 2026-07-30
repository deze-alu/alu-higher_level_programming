#!/usr/bin/python3
"""Defines the City class linked to the cities table."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represents a city stored in the cities table."""

    __tablename__ = "cities"
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

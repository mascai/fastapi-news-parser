from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Post(Base):
    """ News post"""
    __tablename__ = 'posts'

    id  = Column(Integer, primary_key=True)
    site_type = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    

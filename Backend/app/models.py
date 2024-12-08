from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class CV(Base):
    __tablename__ = "cvs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    candidate_name = Column(String, nullable=False)
    skills = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

class JobOffer(Base):
    __tablename__ = "job_offers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    required_skills = Column(String, nullable=False)
    recruiter_id = Column(Integer, ForeignKey("users.id"))

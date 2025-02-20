from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, TIMESTAMP, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=True)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=True)
    dob = Column(String(20), nullable=True)
    password = Column(String(255), nullable=False)
    website = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    subcategory = Column(String(255), nullable=True)
    no_of_employees = Column(String(255), nullable=True)
    step = Column(String(255), nullable=True)
    permissions = Column(Text, nullable=True)
    phone_verified_at = Column(TIMESTAMP, nullable=True)
    email_verified_at = Column(TIMESTAMP, nullable=True)
    term_accepted_at = Column(TIMESTAMP, nullable=True)
    two_factor_secret = Column(String(255), nullable=True)
    is_two_factor_enabled = Column(Boolean, default=False)
    type = Column(Integer, default=0)
    status = Column(Integer, default=1)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now)
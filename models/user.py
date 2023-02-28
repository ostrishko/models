from sqlalchemy import Column, Integer, String, Boolean, Enum
from base_class import Base
import enum


class AccessLevel(enum.Enum):
    worker = 0
    specialist = 1
    engineer = 2
    moderator = 3
    admin = 4


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    patronymic = Column(String, index=True)
    last_name = Column(String, index=True)
    phone_number = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    access_level = Column(Enum(AccessLevel))

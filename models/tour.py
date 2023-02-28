from datetime import datetime
import enum
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Enum, String
from base_class import Base
from sqlalchemy.orm import relationship


class Repeat(enum.Enum):
    once = 0
    daily = 1
    weekly = 2
    mounthly = 3


class Tour(Base):
    id = Column(Integer, index=True, primary_key=True)

    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
    repeat = Column(Enum(Repeat))

    performer = relationship('User', back_populates='tours')

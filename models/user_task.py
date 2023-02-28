import enum
from datetime import datetime

from base_class import Base
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class RequestStatus(enum.Enum):
    pending = 0
    rejected = 1
    in_progress = 2
    completed = 3


class UserTask(Base):
    id = Column(Integer, index=True, primary_key=True)

    creator_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    performer_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    status = Column(Enum(RequestStatus))
    title = Column(String)
    description = Column(String)
    created = Column(DateTime, default=datetime.utcnow)

    creator = relationship('User', back_populates='tasks')
    performer = relationship('User', back_populates='tasks')

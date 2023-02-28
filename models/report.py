from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from base_class import Base
from sqlalchemy.orm import relationship


class Report(Base):
    id = Column(Integer, index=True, primary_key=True)

    created = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    performer = relationship('User', back_populates='reports')

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from base_class import Base
from models.user_task import UserTask


class TaskPhoto(Base):
    id = Column(Integer, index=True, primary_key=True)

    url = Column(String, nullable=False)
    task = relationship(UserTask, back_populates="photos",
                        cascade="all, delete-orphan")

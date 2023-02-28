from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base_class import Base
from models.report import Report


class ReportPhoto(Base):
    id = Column(Integer, index=True, primary_key=True)

    url = Column(String, nullable=False)

    report = relationship(Report, back_populates="photos",
                          cascade="all, delete-orphan")

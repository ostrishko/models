from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from base_class import Base
from models.tour import Tour


class TourPhoto(Base):
    id = Column(Integer, index=True, primary_key=True)

    url = Column(String, nullable=False)
    tour = relationship(Tour, back_populates="photos",
                        cascade="all, delete-orphan")

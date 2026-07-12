from sqlalchemy import Column, Integer, String, Float
from database import Base

class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    level = Column(String, nullable=False)  # "Central" or "State"

    min_age = Column(Integer, nullable=True)
    max_age = Column(Integer, nullable=True)
    max_income = Column(Float, nullable=True)

    occupation = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    caste_category = Column(String, nullable=True)

    state_applicability = Column(String, nullable=False)
    benefits = Column(String, nullable=False)
    official_link = Column(String, nullable=True)
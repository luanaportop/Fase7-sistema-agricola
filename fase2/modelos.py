from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cultura(Base):
    __tablename__ = "Cultura"
    id_cultura   = Column(Integer, primary_key=True)
    nome_cultura = Column(String(100), nullable=False)
    data_plantio = Column(DateTime, nullable=False)
    area_plantio = Column(Float, nullable=False)

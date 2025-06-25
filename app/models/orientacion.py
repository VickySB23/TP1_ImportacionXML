from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.config.database import Base

@dataclass(init=False, repr=True, eq=True)
class Orientacion(Base):
    __tablename__ = 'orientaciones'
    especialidad = Column(Integer, ForeignKey('especialidades.id'), nullable=False)
    plan = Column(Integer, ForeignKey('planes.id'), nullable=False)
    orientacion = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

    especialidad = relationship("Especialidad")
    plan = relationship("Plan")
    materias = relationship("Materia")

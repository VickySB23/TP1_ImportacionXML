from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app import db
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    codigo: Mapped[str] = mapped_column(db.String(20), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(db.String(100), nullable=False)
    creditos: Mapped[Optional[int]] = mapped_column(db.Integer)
    horas_semanales: Mapped[Optional[int]] = mapped_column(db.Integer)
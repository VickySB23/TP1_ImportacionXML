from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Plan(Base):
    __tablename__ = 'planes'
    __table_args__ = (
        PrimaryKeyConstraint('plan', 'especialidad'),
    )
    
    plan = Column('plan', String(20), primary_key=True)  # Parte de PK compuesta
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            plan_node = node.find('plan')
            especialidad_node = node.find('especialidad')
            
            if None in (plan_node, especialidad_node) or not plan_node.text.strip():
                return None

            nombre_node = node.find('nombre')
            nombre = nombre_node.text.strip() if nombre_node is not None and nombre_node.text else None

            return cls(
                plan=plan_node.text.strip(),
                especialidad=int(especialidad_node.text.strip()),
                nombre=nombre
            )
        except Exception as e:
            print(f"Error procesando plan: {e}")
            return None
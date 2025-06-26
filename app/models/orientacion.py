from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Orientacion(Base):
    __tablename__ = 'orientaciones'
    
    id = Column('orientacion', Integer, primary_key=True)
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
    plan = Column(String(20), ForeignKey('planes.plan'), nullable=False)
    nombre = Column(String(100), nullable=False)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            return cls(
                id=int(node.find('orientacion').text.strip()),
                especialidad=int(node.find('especialidad').text.strip()),
                plan=node.find('plan').text.strip(),
                nombre=node.find('nombre').text.strip()
            )
        except Exception as e:
            print(f"Error procesando orientación: {e}")
            return None
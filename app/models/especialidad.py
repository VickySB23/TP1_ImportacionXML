from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Especialidad(Base):
    __tablename__ = 'especialidades'
    
    id = Column('especialidad', Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            return cls(
                id=int(node.find('especialidad').text.strip()),
                nombre=node.find('nombre').text.strip()
            )
        except Exception as e:
            print(f"Error procesando especialidad: {e}")
            return None
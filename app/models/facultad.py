from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Facultad(Base):
    __tablename__ = 'facultades'
    
    id = Column('facultad', Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            return cls(
                id=int(node.find('facultad').text.strip()),
                nombre=node.find('nombre').text.strip()
            )
        except Exception as e:
            print(f"Error procesando facultad: {e}")
            return None
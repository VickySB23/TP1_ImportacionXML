from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Facultad(Base):
    __tablename__ = 'facultades'
    
    facultad = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Extracción directa
            id_node = node.find('facultad')
            nombre_node = node.find('nombre')
            
            # Validación básica
            if None in (id_node, nombre_node) or not all(n.text for n in (id_node, nombre_node)):
                return None
                
            # Conversión de tipos
            try:
                facultad_id = int(id_node.text.strip())
            except ValueError:
                return None
                
            nombre = nombre_node.text.strip()
            
            return cls(facultad=facultad_id, nombre=nombre)
            
        except Exception as e:
            print(f"Error procesando facultad: {e}")
            return None
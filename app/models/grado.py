from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Grado(Base):
    __tablename__ = 'grados'
    
    grado = Column('grado', Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Extracción directa de valores
            grado_node = node.find('grado')
            nombre_node = node.find('nombre')
            
            # Validación de campos requeridos
            if None in (grado_node, nombre_node) or not all(n.text.strip() for n in (grado_node, nombre_node)):
                return None
                
            # Conversión de tipos
            try:
                grado_id = int(grado_node.text.strip())
            except ValueError:
                return None
                
            nombre = nombre_node.text.strip()
            
            return cls(grado=grado_id, nombre=nombre)
            
        except Exception as e:
            print(f"Error procesando grado: {e}")
            return None
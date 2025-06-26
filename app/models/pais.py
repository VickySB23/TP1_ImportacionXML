from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Pais(Base):
    __tablename__ = 'paises'
    
    pais = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Extracción directa de nodos
            pais_node = node.find('pais')
            nombre_node = node.find('nombre')
            
            # Validación de campos requeridos
            if None in (pais_node, nombre_node):
                return None
                
            if not pais_node.text.strip() or not nombre_node.text.strip():
                return None
                
            # Conversión de tipos
            try:
                pais_id = int(pais_node.text.strip())
            except ValueError:
                return None
                
            nombre = nombre_node.text.strip()
            
            return cls(pais=pais_id, nombre=nombre)
            
        except Exception as e:
            print(f"Error procesando país: {e}")
            return None
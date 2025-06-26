from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Universidad(Base):
    __tablename__ = "universidades"
    id = Column('universidad', Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=False)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Mapeo de campos XML (nota: 'universida' en XML vs 'universidad' en BD)
            id_node = node.find('universida')  # Atención: typo en XML ('universida')
            nombre_node = node.find('nombre')
            
            # Validación de campos requeridos
            if None in (id_node, nombre_node):
                return None
            if not id_node.text.strip() or not nombre_node.text.strip():
                return None
                
            # Conversión de valores
            try:
                universidad_id = int(id_node.text.strip())
            except ValueError:
                return None
                
            nombre = nombre_node.text.strip()
            
            return cls(id=universidad_id, nombre=nombre)
            
        except Exception as e:
            print(f"Error procesando universidad: {e}")
            return None
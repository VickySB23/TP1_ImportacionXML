from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Localidad(Base):
    __tablename__ = 'localidades'
    
    id = Column('codigo', Integer, primary_key=True)
    ciudad = Column(String(100), nullable=False)
    provincia = Column(String(100), nullable=False)
    pais_del_c = Column(String(100), nullable=False, default='Argentina')

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Validar campos requeridos
            codigo_node = node.find('codigo')
            ciudad_node = node.find('ciudad')
            provincia_node = node.find('provincia')
            
            if None in (codigo_node, ciudad_node, provincia_node):
                return None

            # Procesar país con valor por defecto
            pais_node = node.find('pais_del_c')
            pais = pais_node.text.strip()[:100] if pais_node is not None and pais_node.text else 'Argentina'

            return cls(
                id=int(codigo_node.text.strip()),
                ciudad=ciudad_node.text.strip(),
                provincia=provincia_node.text.strip(),
                pais_del_c=pais
            )
        except Exception as e:
            print(f"Error procesando localidad: {e}")
            return None
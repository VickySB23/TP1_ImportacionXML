from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Localidad(Base):
    __tablename__ = 'localidades'
    
    codigo = Column(Integer, primary_key=True)
    ciudad = Column(String(100), nullable=False)
    provincia = Column(String(100), nullable=False)  # Cambiado a no nulo según XML
    pais_del_c = Column(String(10), nullable=False, default='Argentina')  # Valor por defecto

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Extracción directa de nodos
            codigo_node = node.find('codigo')
            ciudad_node = node.find('ciudad')
            provincia_node = node.find('provincia')
            pais_node = node.find('pais_del_c')
            
            # Validación de campos obligatorios
            if None in (codigo_node, ciudad_node, provincia_node):
                return None
                
            if not all(n.text.strip() for n in (codigo_node, ciudad_node, provincia_node)):
                return None
            
            # Conversión de tipos
            try:
                codigo = int(codigo_node.text.strip())
            except ValueError:
                return None
                
            ciudad = ciudad_node.text.strip()
            provincia = provincia_node.text.strip()
            
            # Manejo de país (con valor por defecto)
            pais = pais_node.text.strip() if (pais_node is not None and pais_node.text) else 'Argentina'
            
            return cls(
                codigo=codigo,
                ciudad=ciudad,
                provincia=provincia,
                pais_del_c=pais
            )
            
        except Exception as e:
            print(f"Error procesando localidad: {e}")
            return None
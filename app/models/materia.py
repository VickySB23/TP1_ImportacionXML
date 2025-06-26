from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Materia(Base):
    __tablename__ = 'materias'
    especialidad = Column(String(100), nullable=False)
    plan = Column(String(20), nullable=False)
    materia = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=True)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Mapeo de campos XML con sus tipos esperados
            fields_config = {
                'especialidad': {'type': str, 'required': True},
                'plan': {'type': str, 'required': True},
                'materia': {'type': int, 'required': True},
                'nombre': {'type': str, 'required': True},
                'ano': {'type': int, 'required': False}
            }
            
            fields = {}
            
            for field_name, config in fields_config.items():
                xml_element = node.find(field_name)
                
                # Manejo de campos no encontrados
                if xml_element is None or xml_element.text is None:
                    if config['required']:
                        return None
                    fields[field_name] = None
                    continue
                
                # Procesamiento del valor
                value = xml_element.text.strip()
                
                # Conversión de tipo
                try:
                    if config['type'] == int:
                        value = int(value)
                    elif config['type'] == str:
                        value = value
                except ValueError:
                    if config['required']:
                        return None
                    value = None
                
                fields[field_name] = value
            
            return cls(**fields)
            
        except Exception as e:
            print(f"Error al procesar nodo XML: {e}")
            return None
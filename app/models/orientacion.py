from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Orientacion(Base):
    __tablename__ = 'orientaciones'
    
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), primary_key=True, nullable=False)
    plan = Column(Integer, ForeignKey('planes.plan'), primary_key=True, nullable=False)
    orientacion = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Mapeo de campos XML con configuración
            fields_config = {
                'especialidad': {'type': int, 'required': True},
                'plan': {'type': int, 'required': True},
                'orientacion': {'type': int, 'required': True},
                'nombre': {'type': str, 'required': True}
            }
            
            fields = {}
            
            for field_name, config in fields_config.items():
                xml_element = node.find(field_name)
                
                # Validar campos requeridos
                if xml_element is None or xml_element.text is None:
                    if config['required']:
                        return None
                    fields[field_name] = None
                    continue
                
                # Procesar valor
                value = xml_element.text.strip()
                
                # Conversión de tipo
                try:
                    if config['type'] == int:
                        value = int(value)
                    fields[field_name] = value
                except ValueError:
                    if config['required']:
                        return None
                    fields[field_name] = None
            
            # Validar que todos los campos requeridos estén presentes
            if not all(fields.get(f) is not None for f in ['especialidad', 'plan', 'orientacion', 'nombre']):
                return None
                
            return cls(**fields)
            
        except Exception as e:
            print(f"Error al procesar nodo XML de orientación: {e}")
            return None
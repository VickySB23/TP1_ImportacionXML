from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Materia(Base):
    __tablename__ = 'materias'
    
    id = Column('materia', Integer, primary_key=True)
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
    plan = Column(String(20), nullable=False)
    nombre = Column(String(100), nullable=False)
    ano = Column(Integer)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        try:
            # Validación robusta de todos los campos requeridos
            required_fields = {
                'materia': node.find('materia'),
                'especialidad': node.find('especialidad'),
                'plan': node.find('plan'),
                'nombre': node.find('nombre')
            }
            
            # Verificar que todos los campos requeridos existan y tengan contenido
            if any(field is None or not field.text.strip() for field in required_fields.values()):
                return None

            # Procesar campo opcional 'ano'
            ano_node = node.find('ano')
            ano = int(ano_node.text.strip()) if ano_node is not None and ano_node.text.strip().isdigit() else None

            return cls(
                id=int(required_fields['materia'].text.strip()),
                especialidad=int(required_fields['especialidad'].text.strip()),
                plan=required_fields['plan'].text.strip(),
                nombre=required_fields['nombre'].text.strip(),
                ano=ano
            )
        except Exception as e:
            print(f"Error procesando materia: {e}")
            return None
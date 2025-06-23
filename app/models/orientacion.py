from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Orientacion(Base):
    __tablename__ = 'orientaciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=True)
    especialidad_id = Column(Integer, ForeignKey('especialidades.id'), nullable=True)
    plan_id = Column(Integer, ForeignKey('planes.id'), nullable=True)
    # Si necesitas una relación con materias, deberías usar una tabla intermedia (muchos a muchos)

    @classmethod
    def from_xml_node(cls, node: ET.Element):
        fields = {}
        for col in cls.__table__.columns:
            xml_value = node.find(col.name)
            if xml_value is not None and xml_value.text is not None:
                value = xml_value.text.strip()
                if isinstance(col.type, Integer):
                    value = int(value)
                fields[col.name] = value
            else:
                fields[col.name] = None
        return cls(**fields)
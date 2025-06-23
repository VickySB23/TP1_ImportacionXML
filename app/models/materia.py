from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Materia(Base):
    __tablename__ = 'materias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), nullable=True)
    nombre = Column(String(200), nullable=True)
    creditos = Column(Integer, nullable=True)
    horas_semanales = Column(Integer, nullable=True)

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
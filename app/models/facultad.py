from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Facultad(Base):
    __tablename__ = 'facultades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=True)
    abreviatura = Column(String(50), nullable=True)
    directorio = Column(String(100), nullable=True)
    sigla = Column(String(20), nullable=True)
    codigopostal = Column(String(20), nullable=True)
    ciudad = Column(String(100), nullable=True)
    domicilio = Column(String(200), nullable=True)
    telefono = Column(String(50), nullable=True)
    contacto = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)

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
                fields[col.name] = None  # Permite nulos
        return cls(**fields)
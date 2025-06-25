from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Localidad(Base):
    __tablename__ = 'localidades'
    codigo = Column(Integer, primary_key=True)
    ciudad = Column(String(100), nullable=False)
    provincia = Column(String(100))
    pais_del_c = Column(String(10))

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
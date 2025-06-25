from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Universidad(Base):
    __tablename__ = "universidad"
    universidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

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
        return cls(**fields)
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date
from app.config.database import Base
import xml.etree.ElementTree as ET

@dataclass(init=False, repr=True, eq=True)
class Plan(Base):
    __tablename__ = 'planes'
    
    especialidad = Column(Integer, primary_key=True)
    plan = Column(String(20), unique=True)
    nombre = Column(String(100), nullable=True)
    
    @classmethod
    def from_xml_node(cls, node: ET.Element):
        fields = {}
        for col in cls.__table__.columns:
            xml_value = node.find(col.name)
            if xml_value is not None and xml_value.text is not None:
                value = xml_value.text.strip()
                if isinstance(col.type, Integer):
                    value = int(value)
                elif isinstance(col.type, Boolean):
                    value = value.lower() == 'true'
                elif isinstance(col.type, Date):
                    value = datetime.strptime(value, '%Y-%m-%d').date()
                fields[col.name] = value
        return cls(**fields)
from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = 'planes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=True)
    codigo = db.Column(db.String(20), unique=True)
    vigente = db.Column(db.Boolean, default=True)
    fecha_aprobacion = db.Column(db.Date)
    
    @classmethod
    def from_xml_node(cls, node):
        return cls(
            id=int(node.find('id').text),
            nombre=node.find('nombre').text.strip(),
            codigo=node.find('codigo').text.strip(),
            vigente=node.find('vigente').text.strip().lower() == 'true',
            fecha_aprobacion=datetime.strptime(node.find('fecha_aprobacion').text.strip(), '%Y-%m-%d').date()
        )
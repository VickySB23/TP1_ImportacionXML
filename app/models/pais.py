from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pais(db.Model):
    __tablename__ = 'paises'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo_iso = db.Column(db.String(3), unique=True)
    nacionalidad = db.Column(db.String(100))
    
    @classmethod
    def from_xml_node(cls, node):
        return cls(
            id=int(node.find('id').text),
            nombre=node.find('nombre').text.strip(),
            codigo_iso=node.find('codigo_iso').text.strip(),
            nacionalidad=node.find('nacionalidad').text.strip()
        )
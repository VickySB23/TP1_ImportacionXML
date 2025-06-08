from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Localidad(db.Model):
    __tablename__ = 'localidades'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia = db.Column(db.String(100))
    codigo_postal = db.Column(db.String(10))
    
    @classmethod
    def from_xml_node(cls, node):
        return cls(
            id=int(node.find('id').text),
            nombre=node.find('nombre').text.strip(),
            provincia=node.find('provincia').text.strip(),
            codigo_postal=node.find('codigo_postal').text.strip()
        )
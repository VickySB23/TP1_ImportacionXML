import pytest
from app.models.materia import Materia
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def materia_xml_node():
    node = Element('materia')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'codigo').text = 'INF-101'
    SubElement(node, 'nombre').text = ' Algoritmos '
    SubElement(node, 'creditos').text = '8'
    SubElement(node, 'horas_semanales').text = '6'
    return node

def test_materia_from_xml(materia_xml_node):
    mat = Materia.from_xml_node(materia_xml_node)
    
    assert mat.id == 1
    assert mat.codigo == 'INF-101'
    assert mat.nombre == 'Algoritmos'
    assert mat.creditos == 8
    assert mat.horas_semanales == 6

def test_materia_missing_numerics():
    node = Element('materia')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'codigo').text = 'INF-102'
    SubElement(node, 'nombre').text = 'Base de Datos'
    
    mat = Materia.from_xml_node(node)
    
    assert mat.creditos is None
    assert mat.horas_semanales is None
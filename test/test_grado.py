import pytest
from app.models.grado import Grado
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def grado_xml_node():
    node = Element('grado')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' Ingeniería '
    SubElement(node, 'abreviatura').text = 'Ing.'
    SubElement(node, 'nivel').text = 'Universitario'
    return node

def test_grado_from_xml(grado_xml_node):
    grado = Grado.from_xml_node(grado_xml_node)
    
    assert grado.id == 1
    assert grado.nombre == 'Ingeniería'
    assert grado.abreviatura == 'Ing.'
    assert grado.nivel == 'Universitario'

def test_grado_missing_fields():
    node = Element('grado')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Licenciatura'
    
    grado = Grado.from_xml_node(node)
    
    assert grado.id == 2
    assert grado.nombre == 'Licenciatura'
    assert grado.abreviatura is None
    assert grado.nivel is None
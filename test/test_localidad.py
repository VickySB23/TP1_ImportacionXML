import pytest
from app.models.localidad import Localidad
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def localidad_xml_node():
    node = Element('localidad')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' La Plata '
    SubElement(node, 'provincia').text = ' Buenos Aires '
    SubElement(node, 'codigo_postal').text = '1900'
    return node

def test_localidad_from_xml(localidad_xml_node):
    loc = Localidad.from_xml_node(localidad_xml_node)
    
    assert loc.id == 1
    assert loc.nombre == 'La Plata'
    assert loc.provincia == 'Buenos Aires'
    assert loc.codigo_postal == '1900'

def test_localidad_minimal_data():
    node = Element('localidad')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Ensenada'
    
    loc = Localidad.from_xml_node(node)
    
    assert loc.provincia is None
    assert loc.codigo_postal is None
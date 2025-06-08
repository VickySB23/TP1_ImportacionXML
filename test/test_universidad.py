import pytest
from app.models.universidad import Universidad
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def universidad_xml_node():
    node = Element('universidad')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' UNLP '
    SubElement(node, 'codigo').text = 'UNLP001'
    SubElement(node, 'direccion').text = ' Calle 50 '
    return node

def test_universidad_from_xml(universidad_xml_node):
    uni = Universidad.from_xml_node(universidad_xml_node)
    
    assert uni.id == 1
    assert uni.nombre == 'UNLP'
    assert uni.codigo == 'UNLP001'
    assert uni.direccion == 'Calle 50'

def test_universidad_minimal_data():
    node = Element('universidad')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'UTN'
    
    uni = Universidad.from_xml_node(node)
    
    assert uni.id == 2
    assert uni.nombre == 'UTN'
    assert uni.codigo is None
    assert uni.direccion is None
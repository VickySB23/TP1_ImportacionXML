import pytest
from app.models.facultad import Facultad
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def facultad_xml_node():
    node = Element('facultad')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' Facultad de Ingeniería '
    SubElement(node, 'universidad_id').text = '1'
    SubElement(node, 'telefono').text = ' 221-1234567 '
    return node

def test_facultad_from_xml(facultad_xml_node):
    fac = Facultad.from_xml_node(facultad_xml_node)
    
    assert fac.id == 1
    assert fac.nombre == 'Facultad de Ingeniería'
    assert fac.universidad_id == 1
    assert fac.telefono == '221-1234567'

def test_facultad_without_optional():
    node = Element('facultad')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Facultad de Medicina'
    SubElement(node, 'universidad_id').text = '1'
    
    fac = Facultad.from_xml_node(node)
    
    assert fac.telefono is None
import pytest
from app.models.orientacion import Orientacion
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def orientacion_xml_node():
    node = Element('orientacion')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' Ciencias de la Computación '
    SubElement(node, 'especialidad_id').text = '1'
    SubElement(node, 'descripcion').text = ' Orientación en computación '
    return node

def test_orientacion_from_xml(orientacion_xml_node):
    ori = Orientacion.from_xml_node(orientacion_xml_node)
    
    assert ori.id == 1
    assert ori.nombre == 'Ciencias de la Computación'
    assert ori.especialidad_id == 1
    assert ori.descripcion == 'Orientación en computación'

def test_orientacion_without_description():
    node = Element('orientacion')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Inteligencia Artificial'
    SubElement(node, 'especialidad_id').text = '1'
    
    ori = Orientacion.from_xml_node(node)
    
    assert ori.descripcion is None
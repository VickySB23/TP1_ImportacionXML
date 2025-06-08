import pytest
from app.models.pais import Pais
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def pais_xml_node():
    node = Element('pais')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' Argentina '
    SubElement(node, 'codigo_iso').text = 'ARG'
    SubElement(node, 'nacionalidad').text = ' Argentino '
    return node

def test_pais_from_xml(pais_xml_node):
    pais = Pais.from_xml_node(pais_xml_node)
    
    assert pais.id == 1
    assert pais.nombre == 'Argentina'
    assert pais.codigo_iso == 'ARG'
    assert pais.nacionalidad == 'Argentino'

def test_pais_minimal_data():
    node = Element('pais')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Brasil'
    
    pais = Pais.from_xml_node(node)
    
    assert pais.codigo_iso is None
    assert pais.nacionalidad is None
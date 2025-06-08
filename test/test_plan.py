import pytest
from datetime import datetime
from app.models.plan import Plan
from xml.etree.ElementTree import Element, SubElement

@pytest.fixture
def plan_xml_node():
    node = Element('plan')
    SubElement(node, 'id').text = '1'
    SubElement(node, 'nombre').text = ' Plan 2023 '
    SubElement(node, 'codigo').text = 'PL2023'
    SubElement(node, 'vigente').text = 'true'
    SubElement(node, 'fecha_aprobacion').text = '2023-01-15'
    return node

def test_plan_from_xml(plan_xml_node):
    plan = Plan.from_xml_node(plan_xml_node)
    
    assert plan.id == 1
    assert plan.nombre == 'Plan 2023'
    assert plan.codigo == 'PL2023'
    assert plan.vigente is True
    assert plan.fecha_aprobacion == datetime.strptime('2023-01-15', '%Y-%m-%d').date()

def test_plan_missing_dates():
    node = Element('plan')
    SubElement(node, 'id').text = '2'
    SubElement(node, 'nombre').text = 'Plan 2020'
    SubElement(node, 'codigo').text = 'PL2020'
    SubElement(node, 'vigente').text = 'false'
    
    plan = Plan.from_xml_node(node)
    
    assert plan.fecha_aprobacion is None
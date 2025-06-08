import pytest
from xml.etree.ElementTree import Element, SubElement
from app.models.especialidad import Especialidad
from app import create_app, db

@pytest.fixture(scope='module')
def test_app():
    # Configuración de la aplicación para testing
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:password@localhost/test_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def sample_especialidad_data():
    return {
        'nombre': 'Inteligencia Artificial',
        'letra': 'A',
        'observacion': 'Enfoque en machine learning'
    }

@pytest.fixture
def sample_especialidad_xml():
    node = Element('especialidad')
    SubElement(node, 'id').text = '101'
    SubElement(node, 'nombre').text = ' Ciencia de Datos '
    SubElement(node, 'letra').text = ' C '
    SubElement(node, 'observacion').text = ' Análisis de grandes volúmenes '
    return node

class TestEspecialidadModel:
    def test_especialidad_creation(self, test_app, sample_especialidad_data):
        with test_app.app_context():
            especialidad = Especialidad(**sample_especialidad_data)
            db.session.add(especialidad)
            db.session.commit()
            
            assert especialidad.id is not None
            assert especialidad.nombre == 'Inteligencia Artificial'
            assert especialidad.letra == 'A'
            assert especialidad.observacion == 'Enfoque en machine learning'

    def test_required_fields(self, test_app):
        with test_app.app_context():
            # Test que nombre y letra son obligatorios
            with pytest.raises(Exception):
                especialidad = Especialidad(nombre=None, letra='B')
                db.session.add(especialidad)
                db.session.commit()
            
            with pytest.raises(Exception):
                especialidad = Especialidad(nombre='Robotica', letra=None)
                db.session.add(especialidad)
                db.session.commit()

    def test_from_xml_node(self, sample_especialidad_xml):
        especialidad = Especialidad.from_xml_node(sample_especialidad_xml)
        
        assert especialidad.id == 101
        assert especialidad.nombre == 'Ciencia de Datos'
        assert especialidad.letra == 'C'
        assert especialidad.observacion == 'Análisis de grandes volúmenes'

    def test_from_xml_missing_fields(self):
        node = Element('especialidad')
        SubElement(node, 'id').text = '102'
        SubElement(node, 'nombre').text = 'Seguridad Informática'
        
        especialidad = Especialidad.from_xml_node(node)
        
        assert especialidad.id == 102
        assert especialidad.nombre == 'Seguridad Informática'
        assert especialidad.letra is None
        assert especialidad.observacion is None

    def test_string_representation(self, sample_especialidad_data):
        especialidad = Especialidad(**sample_especialidad_data)
        assert str(especialidad) == f"<Especialidad {especialidad.id}: {especialidad.nombre}>"

    def test_equality_comparison(self, sample_especialidad_data):
        esp1 = Especialidad(**sample_especialidad_data)
        esp2 = Especialidad(**sample_especialidad_data)
        
        assert esp1 == esp1  # Misma instancia
        assert esp1 != esp2  # Diferentes instancias (aunque mismos datos)
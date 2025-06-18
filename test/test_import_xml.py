import pytest
from app.services.import_xml import import_xml_to_db
from app.models.pais import Pais
from app.config.database import Base, SessionLocal, engine

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()

def test_import_paises(db_session, tmp_path):
    xml_content = """
    <paises>
        <pais>
            <id>1</id>
            <nombre>Argentina</nombre>
            <codigo_iso>ARG</codigo_iso>
            <nacionalidad>Argentina</nacionalidad>
        </pais>
        <pais>
            <id>2</id>
            <nombre>Brasil</nombre>
            <codigo_iso>BRA</codigo_iso>
            <nacionalidad>Brasileña</nacionalidad>
        </pais>
    </paises>
    """
    xml_file = tmp_path / "paises.xml"
    xml_file.write_text(xml_content)
    cantidad = import_xml_to_db(Pais, str(xml_file), db_session)
    assert cantidad == 2
    assert db_session.query(Pais).count() == 2
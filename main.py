from sqlalchemy.exc import IntegrityError, DataError
from app.config.database import SessionLocal, Base, engine
from app.services.import_xml import import_xml_to_db
from app.models import (
    Pais, Grado, Universidad, Facultad, Materia,
    Localidad, Especialidad, Orientacion, Plan
)

# Orden de importación según dependencias
MODELOS_Y_ARCHIVOS = [
    (Pais, "data/paises.xml"),
    (Grado, "data/grados.xml"),
    (Universidad, "data/universidad.xml"),
    (Facultad, "data/facultades.xml"),
    (Especialidad, "data/especialidades.xml"),
    (Plan, "data/planes.xml"),
    (Localidad, "data/localidades.xml"),
    (Materia, "data/materias.xml"),
    (Orientacion, "data/orientaciones.xml")
]

def main():
    # Crear tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    
    # Importar cada archivo
    for modelo, archivo in MODELOS_Y_ARCHIVOS:
        session = SessionLocal()
        try:
            print(f"Procesando {archivo}...")
            cantidad = import_xml_to_db(modelo, archivo, session)
            session.commit()
            print(f"✅ {modelo.__name__}: {cantidad} registros importados")
        except IntegrityError as e:
            session.rollback()
            print(f"⚠️ Error de datos duplicados en {archivo}: {str(e)}")
        except DataError as e:
            session.rollback()
            print(f"⚠️ Error de tipo de datos en {archivo}: {str(e)}")
        except AttributeError as e:
            session.rollback()
            print(f"⚠️ Error en el XML {archivo} (campo faltante): {str(e)}")
        except Exception as e:
            session.rollback()
            print(f"❌ Error inesperado en {archivo}: {str(e)}")
        finally:
            session.close()

if __name__ == "__main__":
    main()
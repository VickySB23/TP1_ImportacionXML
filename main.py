from app.config.database import SessionLocal
from app.services.import_xml import import_xml_to_db
from app.models import (
    Pais, Grado, Universidad, Facultad, Materia,
    Localidad, Especialidad, Orientacion, Plan
)

MODELOS_Y_ARCHIVOS = [
    (Pais, "data/paises.xml"),
    (Grado, "data/grados.xml"),
    (Universidad, "data/universidad.xml"),
    (Facultad, "data/facultades.xml"),
    (Materia, "data/materias.xml"),
    (Localidad, "data/localidades.xml"),
    (Especialidad, "data/especialidades.xml"),
    (Orientacion, "data/orientaciones.xml"),
    (Plan, "data/planes.xml"),
]

def main():
    session = SessionLocal()
    for modelo, archivo in MODELOS_Y_ARCHIVOS:
        try:
            cantidad = import_xml_to_db(modelo, archivo, session)
            print(f"{modelo.__name__}: {cantidad} registros importados desde {archivo}")
        except Exception as e:
            print(f"Error importando {archivo}: {e}")
    session.close()

if __name__ == "__main__":
    main()
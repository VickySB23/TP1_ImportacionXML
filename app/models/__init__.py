from app.config.database import Base  # Importa Base primero

# Luego importa tus modelos
from .especialidad import Especialidad
from .materia import Materia
from .facultad import Facultad
from .grado import Grado
from .localidad import Localidad
from .orientacion import Orientacion
from .pais import Pais
from .plan import Plan
from .universidad import Universidad

__all__ = [
    'Especialidad',
    'Materia',
    'Facultad',
    'Grado',
    'Localidad',
    'Orientacion',
    'Pais',
    'Plan',
    'Universidad'
]
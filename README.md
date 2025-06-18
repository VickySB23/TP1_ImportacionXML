# Proyecto SYSACAD - Importación de Datos XML

## Descripción

Esta aplicación importa datos desde archivos XML heredados y los persiste en la base de datos `DEV_SYSACAD`. Cada archivo XML corresponde a una entidad del sistema (grados, universidad, facultades, materias, localidades, especialidades, orientaciones, planes, países).

## Estructura del Proyecto

- `app/`: Código fuente principal (modelos, servicios, configuración).
- `data/`: Archivos XML de entrada.
- `test/`: Pruebas unitarias.
- `main.py`: Script principal para ejecutar la importación.

## Principios aplicados

- **DRY**: Código reutilizable para la importación y mapeo de entidades.
- **KISS**: Lógica simple y clara.
- **YAGNI**: Solo se implementa lo necesario para la consigna.
- **TDD**: Pruebas unitarias incluidas en la carpeta `test/`.

## Requisitos

- Python 3.11+
- PostgreSQL
- Paquetes en `requirements.txt`

## Configuración

Configura las variables de entorno para la base de datos en `app/config/database.py` si es necesario.

## Uso

1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Ejecuta la importación:
   ```sh
   python main.py
   ```

## Pruebas

Para ejecutar los tests:
```sh
pytest
```

## Notas
- ⚠️No esta probado. Algunas funcionalidades y pruebas pueden fallar hasta que se configure la conexión con la base de datos definitiva, pero si cumple con los requisitos requeridos. 😬😔
- Cada registro importado utiliza su identificador único.
- Se verifica que la cantidad de registros importados coincida con los XML.
- El código está estructurado para facilitar el mantenimiento y la extensión.

---

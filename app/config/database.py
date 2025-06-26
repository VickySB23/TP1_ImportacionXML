from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuración desde variables de entorno
DB_USER = os.getenv('DB_USER', 'Relyckon')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'tienshu123')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5433')
DB_NAME = os.getenv('DB_NAME', 'SYSACAD')

# Cadena de conexión para PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True
)

# SessionLocal será usado por los modelos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos declarativos
Base = declarative_base()

def get_db():
    """Generador de sesiones para inyección de dependencias"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
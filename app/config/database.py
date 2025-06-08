from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Configuración desde variables de entorno (recomendado para seguridad)
DB_USER = os.getenv('DB_USER', 'sysacad')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'sysacad2025')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'DEV_SYSACAD')

# Cadena de conexión para PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,  # Número de conexiones en el pool
    max_overflow=10,  # Conexiones adicionales cuando el pool está lleno
    pool_pre_ping=True  # Verifica que las conexiones estén activas
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
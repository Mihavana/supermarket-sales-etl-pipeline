from sqlalchemy import create_engine

DB_USER = 'mihavana'
DB_PASSWORD = 'password123'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'supermarket_dw'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
ENGINE = create_engine(DATABASE_URL)

def get_db_engine():
    """Retourne l'objet moteur SQLAlchemy."""
    return ENGINE
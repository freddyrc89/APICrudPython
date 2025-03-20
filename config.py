from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u911718531_senati:S3nati123@srv1851.hstgr.io/u911718531_moviles20251'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración para evitar que la conexión a MySQL se cierre por inactividad
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,   # Verifica si la conexión sigue activa antes de usarla
    "pool_recycle": 280,     # Reinicia conexiones inactivas después de 280 segundos
    "pool_size": 10,         # Número de conexiones activas en el pool
    "max_overflow": 20       # Conexiones adicionales si el pool está lleno
}

db = SQLAlchemy(app)
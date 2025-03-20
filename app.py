#### 6. `app.py` (Punto de Entrada)

from flask import Flask
from config import app, db
from models.database import init_db
from routes.usuario_routes import usuario_bp

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
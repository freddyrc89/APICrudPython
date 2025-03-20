#### 3. `models/usuario.py` (Modelo de Usuario)

from config import db

def init_db():
    db.create_all()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "correo": self.correo}
from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {'extend_existing': True}  # Evita el error de redefinición

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "correo": self.correo}
from flask import jsonify, request
from models.Usuario import Usuario
from config import db

class UsuarioController:
    @staticmethod
    def obtener_usuarios():
        usuarios = Usuario.query.all()
        return jsonify([usuario.to_json() for usuario in usuarios])

    @staticmethod
    def obtener_usuario(id):
        usuario = Usuario.query.get(id)
        if usuario:
            return jsonify(usuario.to_json())
        return jsonify({"mensaje": "Usuario no encontrado en la BaDa"}), 404

    @staticmethod
    def crear_usuario():
        data = request.json
        nuevo_usuario = Usuario(nombre=data['nombre'], correo=data['correo'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(nuevo_usuario.to_json()), 201

    @staticmethod
    def actualizar_usuario(id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404
        
        data = request.json
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.correo = data.get('correo', usuario.correo)
        db.session.commit()
        return jsonify(usuario.to_json())

    @staticmethod
    def eliminar_usuario(id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404
        
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
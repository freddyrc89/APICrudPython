from flask import Blueprint
from controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.add_url_rule('/usuarios', 'obtener_usuarios', UsuarioController.obtener_usuarios, methods=['GET'])
usuario_bp.add_url_rule('/usuarios/<int:id>', 'obtener_usuario', UsuarioController.obtener_usuario, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', 'crear_usuario', UsuarioController.crear_usuario, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>', 'actualizar_usuario', UsuarioController.actualizar_usuario, methods=['PUT'])
usuario_bp.add_url_rule('/usuarios/<int:id>', 'eliminar_usuario', UsuarioController.eliminar_usuario, methods=['DELETE'])



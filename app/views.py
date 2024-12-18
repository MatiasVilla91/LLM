from flask import Blueprint, request, jsonify
from .chatbot import obtener_respuesta

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/', methods=['POST'])  # Ahora la ruta es solo '/chat'
def chat():
    datos = request.json
    mensaje = datos.get('mensaje', '')
    respuesta = obtener_respuesta(mensaje)
    return jsonify({"respuesta": respuesta})

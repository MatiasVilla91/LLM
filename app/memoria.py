import json
import os
import re
from datetime import datetime

MEMORIA_FILE = "memoria.json"
memoria={}

def cargar_memoria():
    try:
        with open(MEMORIA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo memoria.json no encontrado. Creando uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print("Error: Archivo memoria.json corrupto. Reiniciando memoria.")
        return {}

def guardar_memoria(memoria):
    try:
        # Solo crea el directorio si hay una ruta en MEMORIA_FILE
        directorio = os.path.dirname(MEMORIA_FILE)
        if directorio:  # Si no es una cadena vacía
            os.makedirs(os.path.dirname(MEMORIA_FILE), exist_ok=True)
        with open(MEMORIA_FILE, "w") as file:
            json.dump(memoria, file, indent=10, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar la memoria: {e}")

def manejar_conversacion(usuario, mensaje):
    if usuario not in memoria:
        memoria[usuario] = {"nombre": None, "historial": []}

    # Registrar mensaje del usuario
    memoria[usuario]["historial"].append({"usuario": mensaje})

    # Intentar extraer nombre
    match = re.search(r"me llamo ([a-zA-Z]+)", mensaje, re.IGNORECASE)
    if match:
        nombre = match.group(1).strip()
        memoria[usuario]["nombre"] = nombre
        respuesta = f"¡Encantado, {nombre}! Ahora te recordaré."
    else:
        nombre = memoria[usuario].get("nombre")
        if nombre:
            respuesta = f"Hola de nuevo, {nombre}. ¿En qué puedo ayudarte hoy?"
        else:
            respuesta = "Hola, ¿cómo te llamas?"

    # Registrar respuesta del bot
    memoria[usuario]["historial"].append({"bot": respuesta})
    guardar_memoria(memoria)
    return respuesta


# Evitar sobrescritura entre sesiones defiriendo la escritura al archivo a menos que haya cambios
class MemoriaPersistente:
    def __init__(self):
        self.memoria = cargar_memoria()
        self.cambios = False

    def obtener_memoria(self):
        return self.memoria

    def actualizar_memoria(self, usuario, datos):
        self.memoria[usuario] = datos
        self.cambios = True

    def guardar_si_cambios(self):
        if self.cambios:
            guardar_memoria(self.memoria)
            self.cambios = False

memoria_global = MemoriaPersistente()

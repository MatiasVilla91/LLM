from transformers import pipeline, MarianMTModel, MarianTokenizer
from .memoria import cargar_memoria, guardar_memoria, manejar_conversacion  # Importar funciones de memoria

# Configuración de Blenderbot
generador = pipeline('text2text-generation', model='facebook/blenderbot-400M-distill')

# Configuración de traductores
translator_es_to_en = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-es-en")
tokenizer_es_to_en = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")
translator_en_to_es = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es")
tokenizer_en_to_es = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")

# Funciones de traducción
def traducir_a_ingles(texto):
    inputs = tokenizer_es_to_en(texto, return_tensors="pt", max_length=512, truncation=True)
    outputs = translator_es_to_en.generate(**inputs)
    return tokenizer_es_to_en.decode(outputs[0], skip_special_tokens=True)

def traducir_a_espanol(texto):
    inputs = tokenizer_en_to_es(texto, return_tensors="pt", max_length=512, truncation=True)
    outputs = translator_en_to_es.generate(**inputs)
    return tokenizer_en_to_es.decode(outputs[0], skip_special_tokens=True)

# Obtener respuesta del bot con traducciones
def obtener_respuesta(mensaje, usuario="default_user"):
    # Traducir entrada al inglés
    mensaje_en_ingles = traducir_a_ingles(mensaje)
    
    # Generar respuesta con Blenderbot
    respuesta_en_ingles = generador(f"User: {mensaje_en_ingles} Bot:", max_length=100, do_sample=True)[0]['generated_text']
    
    # Traducir respuesta al español
    respuesta_en_espanol = traducir_a_espanol(respuesta_en_ingles)
    # Manejar memoria de conversación
    respuesta_con_memoria = manejar_conversacion(usuario, mensaje)
    return f"{respuesta_con_memoria} {respuesta_en_espanol}"

# Bucle de conversación
if __name__ == "__main__":
    print("¡Bienvenido al chatbot! Escribe 'salir' para terminar la conversación.")
    usuario = "12345" 
    memoria = cargar_memoria()
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ["salir", "exit"]:
            print("¡Adiós!")
            break
        respuesta = obtener_respuesta(mensaje, usuario)
        print(f"Bot: {respuesta}")
        guardar_memoria(memoria)  # Guardar memoria actualizada
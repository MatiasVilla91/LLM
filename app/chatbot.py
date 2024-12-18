from transformers import pipeline

# Usamos Hugging Face como ejemplo
generador = pipeline('text2text-generation', model='facebook/blenderbot-400M-distill')

def obtener_respuesta(mensaje):
    respuesta = generador(f"User: {mensaje} Bot:", max_length=100, do_sample=True)
    return respuesta[0]['generated_text']

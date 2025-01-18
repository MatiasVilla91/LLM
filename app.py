import os
from app import create_app

# Desactivar GPU para evitar conflictos en TensorFlow (si es relevante)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Crear la aplicación Flask
app = create_app()

# Ejecutar el servidor
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Usar el puerto definido por Render o 5000 como predeterminado
    app.run(host="0.0.0.0", port=port, debug=True)

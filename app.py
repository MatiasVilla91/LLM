import os
from app import create_app

# Crear la aplicación Flask
app = create_app()

# Ejecutar el servidor
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Puerto especificado por Render o 5000 por defecto
    app.run(host="0.0.0.0", port=port, debug=True)

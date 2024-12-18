from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
    db.init_app(app)

    # Registrar blueprints
    from .views import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')

    # Ruta para la página de inicio
    @app.route('/')
    def home():
        return render_template('index.html')  # Correcta ruta para cargar la plantilla

    return app

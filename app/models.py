from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conversacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje_usuario = db.Column(db.String(256), nullable=False)
    respuesta_bot = db.Column(db.String(256), nullable=False)

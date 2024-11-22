from flask_sqlalchemy import SQLAlchemy

# Créez une instance de la base de données SQLAlchemy
db = SQLAlchemy()

# Définissez la classe TablesRestaurant pour représenter la table "tables_restaurant"
class TablesRestaurant(db.Model):
    __tablename__ = 'tables_restaurant'

    id_table = db.Column(db.Integer, primary_key=True)
    numero_table = db.Column(db.Integer, nullable=False)
    nombre_place = db.Column(db.Integer, nullable=False)
    occupe = db.Column(db.Boolean, default=False)

    def __init__(self, numero_table, nombre_place, occupe=False):
        self.numero_table = numero_table
        self.nombre_place = nombre_place
        self.occupe = occupe

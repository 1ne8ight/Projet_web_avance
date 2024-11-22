from flask_sqlalchemy import SQLAlchemy

# Créez une instance de la base de données SQLAlchemy
db = SQLAlchemy()
# Définissez la classe Categories pour représenter la table "categories"
class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    nom_categorie = db.Column(db.String(100))

    def __init__(self, nom_categorie):
        self.nom_categorie = nom_categorie


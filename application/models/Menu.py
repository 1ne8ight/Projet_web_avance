from flask_sqlalchemy import SQLAlchemy

# Créez une instance de la base de données SQLAlchemy
db = SQLAlchemy()


# Définissez la classe Menu pour représenter la table "menu"
class Menu(db.Model):
    __tablename__ = 'menu'

    id_menu = db.Column(db.Integer, primary_key=True)
    nom_plat = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(225))
    categories = db.Column(db.String(100))

    def __init__(self, nom_plat, prix, image=None, categories=None):
        self.nom_plat = nom_plat
        self.prix = prix
        self.image = image
        self.categories = categories


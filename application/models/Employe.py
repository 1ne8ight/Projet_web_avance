from flask_sqlalchemy import SQLAlchemy

# Créez une instance de la base de données SQLAlchemy
db = SQLAlchemy()

# Définissez la classe Categories pour représenter la table "Employe"

class Employe(db.Model):
    __tablename__ = 'employe'

    id_employe = db.Column(db.Integer, primary_key=True)
    nom_employe = db.Column(db.String(255), nullable=False)
    prenom_employe = db.Column(db.String(255))
    email_employe = db.Column(db.String(255), nullable=False)
    poste_employe = db.Column(db.String(255), nullable=False)
    numero_telephone = db.Column(db.String(30), nullable=False)
    ville_employe = db.Column(db.String(255), nullable=False)
    date_naissance_employe = db.Column(db.String(10))
    password_employe = db.Column(db.String(255), nullable=False)
    acces = db.Column(db.Enum('admin', 'employe'))
    image_employe = db.Column(db.String(255))
    matricule_employe = db.Column(db.String(50), nullable=False)
    date_embauche = db.Column(db.DateTime)
    actif = db.Column(db.Boolean)

    def __init__(self, nom_employe, prenom_employe, email_employe, poste_employe, numero_telephone, ville_employe, date_naissance_employe, password_employe, acces, image_employe, matricule_employe, date_embauche, actif):
        self.nom_employe = nom_employe
        self.prenom_employe = prenom_employe
        self.email_employe = email_employe
        self.poste_employe = poste_employe
        self.numero_telephone = numero_telephone
        self.ville_employe = ville_employe
        self.date_naissance_employe = date_naissance_employe
        self.password_employe = password_employe
        self.acces = acces
        self.image_employe = image_employe
        self.matricule_employe = matricule_employe
        self.date_embauche = date_embauche
        self.actif = actif
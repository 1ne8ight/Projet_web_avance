from flask_sqlalchemy import SQLAlchemy

# Créez une instance de la base de données SQLAlchemy
db = SQLAlchemy()


# Définissez la classe Categories pour représenter la table "commande"

class Commande(db.Model):
    __tablename__ = 'commande'
    
    id_commande = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(255), nullable=False)
    contenu_commande = db.Column(db.Text)
    date_commande = db.Column(db.String(25))
    matricule_employe = db.Column(db.String(50))
    recu_commande = db.Column(db.String(255))
    total_commande = db.Column(db.Float)
    statuts = db.Column(db.Boolean)
    numero_table = db.Column(db.Integer)
    montant_recu = db.Column(db.Float)
    monnaie = db.Column(db.Float)
    cuisine = db.Column(db.Boolean)
    
    def __init__(self, nom_client, contenu_commande, date_commande, matricule_employe, recu_commande, total_commande, statuts, numero_table, montant_recu, monnaie, cuisine):
        self.nom_client = nom_client
        self.contenu_commande = contenu_commande
        self.date_commande = date_commande
        self.matricule_employe = matricule_employe
        self.recu_commande = recu_commande
        self.total_commande = total_commande
        self.statuts = statuts
        self.numero_table = numero_table
        self.montant_recu = montant_recu
        self.monnaie = monnaie
        self.cuisine = cuisine

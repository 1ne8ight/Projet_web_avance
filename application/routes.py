import json
from application import app
from flask import Response, make_response, render_template, redirect, url_for, request, session, send_file, jsonify, flash
# from application.config import Config
from application.config import Config_bdd, key
from flask_mysqldb import MySQL
import MySQLdb.cursors
from passlib.hash import sha256_crypt
from flask_socketio import SocketIO, emit
from flask_compress import Compress
import time
from flask_caching import Cache
import numpy as np
import joblib
import sklearn
import pandas as pd
from babel.numbers import format_currency

# Fonction pour convertir un nombre en FCFA
def convert_to_fcfa(number):
    formatted_number = format_currency(number, 'XOF', locale='fr_FR')
    return formatted_number

# from datetime import datetime
# from application import models

# from application.models

# from flask_socketio import SocketIO, emit

socketio = SocketIO(app)

# from application.functions import getTable
# app.secret_key = 'xyzsdfg'
app.secret_key = key
from fpdf import FPDF
import datetime
import os
import random
# socketio = SocketIO(app)
# ne pas oublier que tu as ajouter une npuvelle colonne date_embauche
# Configuration du cache
app.config['CACHE_TYPE'] = 'simple' 
app.config.from_object(Config_bdd)


mysql = MySQL(app)
cache = Cache(app)

current_date = str(datetime.date.today())
print(current_date)

@app.route('/')
@app.route('/signin', methods=['GET', 'POST'])
def signin():

    print("| ", sha256_crypt.encrypt(str("1234")), " |")
    message = ''
    if request.method == 'POST' and 'matricule' in request.form and 'password' in request.form :
        matricule = request.form['matricule']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM employe WHERE matricule_employe = %s', (matricule,))
        employe =  cursor.fetchone()

        if employe:
            if sha256_crypt.verify(password, employe['password_employe']):
                session['logged_in'] = True
                session['id_employe'] = employe['id_employe']
                session['nom_employe'] = employe['nom_employe']
                session['prenom_employe'] = employe['prenom_employe']
                session['email'] = employe['email_employe']
                session['poste'] = employe['poste_employe']
                session['numero_telephone'] = employe['numero_telephone']
                session['ville_employe'] = employe['ville_employe']
                session['date_naissance_employe'] = employe['date_naissance_employe']
                session['acces'] = employe['acces']
                session['image_employe'] = employe['image_employe']
                session['matricule_employe'] = employe['matricule_employe']

                cursor = mysql.connection.cursor()
                cursor.execute('UPDATE employe SET actif = 1 WHERE id_employe = %s', (session['id_employe'],))
                mysql.connection.commit()

                message = 'Vous etes connectée'

                if session['acces'] == 'admin':
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('interface_employe'))

            else:
                message = 'Matricule ou mot de passe incorrect !!'
    return render_template('signin.html', message=message)

@app.route('/logout')
def logout():
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE employe SET actif = 0 WHERE id_employe = %s', (session['id_employe'],))
    mysql.connection.commit()
    session.clear()
    return redirect(url_for('signin'))

@app.route('/dashboard', methods=['GET', 'POST'])
# @cache.cached(timeout=60)  
def dashboard():

    
    cursor = mysql.connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE)=%s', (current_date,))
    count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM commande WHERE statuts = FALSE AND CONVERT(date_commande, DATE)=%s', (current_date,))
    no_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM employe WHERE actif = 1')
    actif = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM employe')
    nbre_employe = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE)=%s', (current_date,))
    chiffre_affaire = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE statuts = TRUE ')
    chiffre_affaire_gobal = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM commande WHERE statuts = TRUE')
    commande_globale = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE statuts = FALSE AND CONVERT(date_commande, DATE)=%s', (current_date,))
    non_valide = cursor.fetchone()[0]

    if chiffre_affaire is not None:
        print('not none')
    else:
        chiffre_affaire = 0

    if non_valide is not None:
        print('not none')
    else:
        non_valide = 0

    
    
    
    date = datetime.date.today()
    jour = datetime.date.today().day
    mois = datetime.date.today().month
    predict_donnee = pd.DataFrame({'mois': [mois], 
                                  'jour': [jour]})

    chemin_modele = "application\static\GradientBRCommande.sav"
    model = joblib.load(chemin_modele)
    predict_commande = model.predict(predict_donnee)[0]

    return render_template('dashboard.html', ventes=count, chiffre_affaire=convert_to_fcfa(float(chiffre_affaire)), actif=actif, no_ventes=no_count, non_valide=convert_to_fcfa(float(non_valide)), nbre_employe=nbre_employe, chiffre_affaire_gobal=convert_to_fcfa(float(chiffre_affaire_gobal)), commande_globale=commande_globale, date= date, predict_commande=int(predict_commande))

# @app.route("/heure")
# def h():
#     current_date = datetime.date.today()
#     return "hello " + str(current_date)

# CRUD employe
@app.route('/employe')
# @cache.cached(timeout=60)  
def employe():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM employe WHERE matricule_employe != %s', (session['matricule_employe'],))
    data = cursor.fetchall()
    cursor.close()
    return render_template('employe.html', employees=data)


app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Vérifier si l'extension du fichier est autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_matricule(nom):
    matricule = nom.upper().replace(' ', '')  # Convertir en majuscules et supprimer les espaces
    matricule += str(random.randint(1000, 9999))  # Ajouter un nombre aléatoire entre 1000 et 9999
    return matricule
@app.route('/AjouterEmploye')
def AfficherEmploye():
    return render_template('ajouterEmploye.html')


@app.route('/AjouterEmploye', methods=['POST'])
def AjouterEmploye():

    if request.method == 'POST':
        nom_employe = request.form['nom']
        prenom_employe = request.form['prenom']
        email_employe = request.form['email']
        poste_employe = request.form['poste']
        numero_telephone = request.form['telephone']
        ville_employe = request.form['ville']
        date_naissance_employe = request.form['date_naissance']
        photo_employe = request.files['photo']

        matricule_genere = generate_matricule(nom_employe)

        if request.form['mdp'] == request.form['mdpC']:
            password_employe = sha256_crypt.encrypt(str(request.form['mdpC']))
    
        acces = request.form['acces']

        if photo_employe and allowed_file(photo_employe.filename):
            filename = photo_employe.filename
            photo_employe.save(os.path.join("application/static/images/employe_image", filename))

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO employe(nom_employe, prenom_employe, email_employe, poste_employe, numero_telephone, ville_employe, date_naissance_employe, password_employe, acces, image_employe, matricule_employe, date_embauche, actif) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (nom_employe, prenom_employe, email_employe, poste_employe, numero_telephone, ville_employe, date_naissance_employe, password_employe, acces, filename, matricule_genere, current_date, 0))
        
        mysql.connection.commit()
        return redirect(url_for('employe'))

@app.route('/employe/edit_admin')
def UpdateAdmin():
    # cursor = mysql.connection.cursor()
    # cursor.execute('SELECT * FROM employe WHERE id_employe = %s', (id))
    # data = cursor.fetchall()
    # cursor.close()
    return render_template('edit_admin.html')

@app.route('/edit_employe/<id>', methods=['POST', 'GET'])
def UpdateEmploye(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM employe WHERE id_employe = %s', (id,))
    data = cursor.fetchall()
    cursor.close()
    return render_template('edit_employe.html', employe=data[0])

@app.route('/employe/<id>', methods=['POST', 'GET'])
def DeleteEmploye(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM employe WHERE id_employe = %s', (id,))
    mysql.connection.commit()

    return redirect(url_for('employe'))


# Fin CRUD employe

#Crud table
@app.route('/table')
def tables():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tables_restaurant')
    data = cursor.fetchall()
    cursor.close()
    return render_template('tables.html', tables=data)

@app.route('/tables/ajouter', methods=['POST'])
def AjouterTable():
    if request.method == 'POST':
        numero_table = request.form['numero_table']
        nombre_place = request.form['nombre_place']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tables_restaurant(numero_table, nombre_place, occupe) VALUES (%s, %s, %s)", 
                       (numero_table, nombre_place, 0))
        
        mysql.connection.commit()
        return redirect(url_for('tables'))
    
@app.route('/tables/<id>', methods=['POST', 'GET'])
def DeleteTable(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tables_restaurant WHERE id_table = %s', (id,))
    mysql.connection.commit()

    return redirect(url_for('tables'))

@app.route('/tables/updateTable', methods=['POST', 'GET'])
def updateTable():
    if request.method == 'POST':
        if 'bt_modif' in request.form:
            id_table = request.form['id_modif_table']
            numero_table = request.form['numero_table_modif']
            nbre_place = request.form['nombre_place_modif']
            occupe = request.form['occupe_modif']
            
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE tables_restaurant SET numero_table = %s, nombre_place = %s, occupe = %s WHERE id_table = %s', (numero_table, nbre_place, occupe ,id_table))
            mysql.connection.commit()

    return redirect(url_for('tables'))

#Fin Crud table


#Crud menu
@app.route('/menu')
# @cache.cached(timeout=240)  
def menu():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu')
    data = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    cursor.close()

    return render_template('menu.html', menus=data, categories=categories)

@app.route('/menu/ajouter', methods=['POST'])
def AjouterMenu():
    if request.method == 'POST':
        nom_plat = request.form['nom_plat']
        menu_image = request.files['menu_image']
        prix = request.form['prix']
        categorie = request.form['categorie']
        

        if menu_image and allowed_file(menu_image.filename):
            filename = menu_image.filename
            menu_image.save(os.path.join("application/static/images/menu_image", filename))

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO menu(nom_plat, prix, image, categories) VALUES (%s, %s, %s, %s)", 
                       (nom_plat, prix, filename, categorie))
        
        mysql.connection.commit()
        return redirect(url_for('menu'))
    
@app.route('/menu/ajouter_categorie', methods=['POST', 'GET'])
def AjouterCategorie():
    if request.method == 'POST':
        nom_categorie = request.form['nom_categorie']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO categories(nom_categorie) VALUES (%s)",
                       (nom_categorie,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('menu'))
    
@app.route('/menu/<id>', methods=['POST', 'GET'])
def DeleteMenu(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM menu WHERE id_menu = %s', (id,))
    mysql.connection.commit()

    return redirect(url_for('menu'))

@app.route('/menu/updateMenu', methods=['POST', 'GET'])
def updateMenu():
    if request.method == 'POST':
        if 'bt_modif' in request.form:
            nom_plat = request.form['nom_plat_modif']
            prix = request.form['prix_modif']
            categories = request.form['categories_modif']
            id_menu = request.form['id_modif_menu']
            
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE menu SET nom_plat = %s, prix = %s,  categories = %s WHERE id_menu = %s', (nom_plat, prix, categories ,id_menu))
            mysql.connection.commit()

    return redirect(url_for('menu'))

#Fin crud menu


@app.route('/interface_employe/')
def interface_employe():
        cursor = mysql.connection.cursor()
    
        # formatted_time = current_date
        # print(current_date)
        cursor.execute('SELECT COUNT(*) FROM commande WHERE matricule_employe = %s AND CONVERT(date_commande, DATE)=%s', (session['matricule_employe'], current_date))
        count = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM commande WHERE CONVERT(date_commande, DATE)=%s', (current_date,))
        no_count = cursor.fetchone()[0]

        cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE matricule_employe = %s AND CONVERT(date_commande, DATE)=%s', (session['matricule_employe'] ,current_date))
        chiffre_affaire = cursor.fetchone()[0]

        cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE CONVERT(date_commande, DATE)=%s', (current_date,))
        non_valide = cursor.fetchone()[0]

        cursor.execute('SELECT * FROM commande WHERE matricule_employe = %s AND CONVERT(date_commande, DATE)=%s',(session['matricule_employe'],current_date))
        commandes = cursor.fetchall()
        cursor.close()

        if chiffre_affaire is not None:
            print('not none')
        else:
            chiffre_affaire = 0
        if non_valide is not None:
            print('not none')
        else:
            non_valide = 0

        return render_template('interface_employe.html', ventes=count, chiffre_affaire=convert_to_fcfa(float(chiffre_affaire)), no_ventes=no_count, non_valide=convert_to_fcfa(float(non_valide)), commandes=commandes)


@app.route('/commande_enregistrer/<id>', methods=['POST', 'GET'])
def UpdateCommande(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE commande SET statuts  = TRUE WHERE id_commande = %s', (id,))
    mysql.connection.commit()

    cursor.execute('UPDATE tables_restaurant SET occupe  = 0 WHERE numero_table = %s', (getNumTableByCommande(id),))
    mysql.connection.commit()
    socketio.emit('dashboard')


    if session['acces'] == 'employe':
        return redirect(url_for("commande_enregistrer"))
    else :
        return redirect(url_for("commande_admin"))
    
def getNumTableByCommande(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT numero_table FROM commande WHERE id_commande = %s', (id,))
    table = cursor.fetchall()[0]
    cursor.close()
    return table


@app.route('/commande_enregistrer')
def commande_enregistrer():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = TRUE AND matricule_employe = %s AND CONVERT(date_commande, DATE) =%s',(session['matricule_employe'], current_date))
    commande_terminer = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = FALSE AND matricule_employe = %s AND CONVERT(date_commande, DATE) =%s',(session['matricule_employe'], current_date))
    commande_non_terminer = cursor.fetchall()
    cursor.close()

    return render_template('commande_enregistrer.html', terminees = commande_terminer, non_terminees = commande_non_terminer)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        # self.cell(0, 10, 'E-Commande', 0, 1, 'C')
        # Insérez une image
        self.image('application/static/assets/icon.png', x=10, y=10, w=30)
        self.ln(15)
        # self.cell(0, 10, 'Facture', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Passé une agréable journée !!', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', 'I', 9)
        self.multi_cell(0, 10, body)
        self.ln()


def getItemById(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu WHERE id_menu = %s', (id,))
    item = cursor.fetchall()
    return item



@app.route('/commande')
def afficherC():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tables_restaurant WHERE occupe = 0')
    tables = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu')
    menu = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    cursor.close()
    return render_template('commande.html', menu=menu, tables=tables, categories=categories)


@app.route('/commande', methods=['GET', 'POST'])
def commande():
    if request.method == 'POST':
        name = request.form.get('nom_client')
        table = request.form.get('numero_table')
        selected_items = request.form.getlist('item')
        montant_recu = request.form.get('montant_recu')
        # nbre = int(request.form['nbre'])
        number_values = request.form.getlist('nbre')
        vrai = []
        faux = []
        

        print(number_values)
        print(selected_items)
        for i in range(len(number_values)):
            if not number_values[i].strip() :
                faux.append(number_values[i])
            else :
                vrai.append(int(number_values[i]))
        print(vrai)
        print(faux)
        
        total = 0.0
        items = []
        itemstotal = []
        for item_id in selected_items:
            item = getItemById(int(item_id))
            print(int(selected_items.index(item_id)))
            # print(item_id)
            # print(item)
            cm = str(str(vrai[int(selected_items.index(item_id))]) + 'x' + item[0][1])
            items.append(cm)
            total += item[0][2]*int(vrai[int(selected_items.index(item_id))])
            itemstotal.append(item[0][2]*int(vrai[int(selected_items.index(item_id))]))

            
        total = round(total, 2)
        monnaie = (float(montant_recu) - float(total))
        # str(random.randint(1000, 9999))  # Ajouter un nombre aléatoire entre 1000 et 9999

        # pdf = PDF(format='A3')
        pdf = PDF(format=(150, 220)) 
                # Créer un objet PDF

        # pdf = PDF(format='A3')
        pdf.add_page()

        # Entête de la facture
        # pdf.chapter_title('Informations du client:')
        # pdf.cell(0, 10, f'Nom du client: {name}', 0, 1)
        pdf.set_font('Arial', 'I', 9)
        pdf.multi_cell(0, 10, "Informations du client:", align='L')
        pdf.multi_cell(0, 10, f'Nom du client: {name}', align='L')
        pdf.ln(5) 

        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        pdf.multi_cell(0, 10, f'Date de facture: {formatted_time}', align='R')
        pdf.multi_cell(0, 10, f'Numéro de table: {table}', align='R')
        pdf.multi_cell(0, 10, f"Serveur: {session['nom_employe']}", align='R')
        pdf.ln(5)

        # Tableau des articles commandés
        pdf.chapter_title('Items commandés:')
        pdf.set_font('Helvetica', 'BI', 10)
        pdf.cell(90, 10, 'Item', 1)
        pdf.cell(45, 10, 'Prix', 1)
        pdf.ln()
        for item in items:
            pdf.set_text_color(0, 0, 255)
            pdf.set_font('Helvetica', 'BI', 10)
            pdf.cell(90, 10, item, 1)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(45, 10, str(itemstotal[int(items.index(item))]) + ' FCFA', 1)
            pdf.ln()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'I', 9)
        pdf.cell(90, 10, 'Total', 1)
        pdf.cell(45, 10, str(total)+' FCFA', 1)
        pdf.ln(10)

        # Résumé financier
        pdf.set_font('Arial', 'I', 9)
        pdf.chapter_title('Résumé financier:')
        pdf.cell(0, 10, 'Somme reçue: '+str(montant_recu) + ' FCFA', 0, 1, 'R')
        pdf.cell(0, 10, 'Monnaie rendue: ' + str(monnaie) + ' FCFA', 0, 1, 'R')
        # pdf.output("output.pdf")
       
        # pdf.cell(0, 10, 'date : ' + formatted_time , 0, 1)
        pdf_file = 'facture_' + name + '_' + str(random.randint(1000, 9999))+'.pdf'
        pdf_filename = os.path.join("application/static/recu", pdf_file)
        pdf.output(pdf_filename)

        items_total = ", ".join(items)

         #definir le curseur 
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO commande(nom_client, contenu_commande, date_commande, matricule_employe, recu_commande, total_commande, statuts, numero_table, montant_recu, monnaie, cuisine) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, items_total, formatted_time, session['matricule_employe'], pdf_file, total, 0, table, montant_recu, monnaie, 0))
        flash('Commande enregistrer!', 'success')
        mysql.connection.commit()
        
        cursor.execute('UPDATE tables_restaurant SET occupe = 1 WHERE numero_table = %s', (table,))
        mysql.connection.commit()
        cursor.close()
        socketio.emit('connection')
        
    return redirect(url_for("afficherC"))

@app.route('/commande_admin')
def commande_admin():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE) =%s',(current_date,))
    commande_terminer = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = FALSE AND CONVERT(date_commande, DATE) =%s',(current_date,))
    commande_non_terminer = cursor.fetchall()
    cursor.close()
    return render_template('commande_admin.html', terminees = commande_terminer, non_terminees = commande_non_terminer)


@app.route('/graphique_affaire', methods =['GET'])
# @cache.cached(timeout=240)  
def graphique_affaire():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT CASE WHEN MONTH(date_commande) = 1 THEN 'Janvier' WHEN MONTH(date_commande) = 2 THEN 'Février' WHEN MONTH(date_commande) = 3 THEN 'Mars' WHEN MONTH(date_commande) = 4 THEN 'Avril' WHEN MONTH(date_commande) = 5 THEN 'Mai' WHEN MONTH(date_commande) = 6 THEN 'Juin' WHEN MONTH(date_commande) = 7 THEN 'Juillet' WHEN MONTH(date_commande) = 8 THEN 'Août' WHEN MONTH(date_commande) = 9 THEN 'Septembre' WHEN MONTH(date_commande) = 10 THEN 'Octobre' WHEN MONTH(date_commande) = 11 THEN 'Novembre' WHEN MONTH(date_commande) = 12 THEN 'Décembre' ELSE 'Inconnu' END AS mois, SUM(total_commande) AS somme_total_commande FROM commande WHERE statuts=TRUE GROUP BY MONTH(date_commande) ORDER BY MONTH(date_commande)")
        data = cursor.fetchall()
        cursor.close()

        # Transformation des résultats en un format JSON
        data = [{'mois': row[0], 'somme_total': row[1]} for row in data]

        return jsonify(data)
    

@app.route('/graphique_commande_employe', methods =['GET'])
# @cache.cached(timeout=240)  
def graphique_commande_employe():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT matricule_employe, COUNT(*) AS nombre_de_commandes FROM commande GROUP BY matricule_employe")
        data = cursor.fetchall()
        cursor.close()

        # Transformation des résultats en un format JSON
        data = [{'employe': row[0], 'commande': row[1]} for row in data]

        return jsonify(data)
    



@app.route('/graphique_nbr_commande_mois', methods =['GET'])
# @cache.cached(timeout=240)  
def graphique_nbr_commande_mois():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT CASE MONTH(date_commande) WHEN 1 THEN 'Janvier' WHEN 2 THEN 'Février' WHEN 3 THEN 'Mars' WHEN 4 THEN 'Avril' WHEN 5 THEN 'Mai' WHEN 6 THEN 'Juin' WHEN 7 THEN 'Juillet' WHEN 8 THEN 'Août' WHEN 9 THEN 'Septembre' WHEN 10 THEN 'Octobre' WHEN 11 THEN 'Novembre' WHEN 12 THEN 'Décembre' END AS nom_du_mois, COUNT(*) AS nombre_de_commandes FROM commande WHERE statuts = TRUE GROUP BY MONTH(date_commande) ORDER BY MONTH(date_commande)")
        data = cursor.fetchall()
        cursor.close()

        # Transformation des résultats en un format JSON
        data = [{'nom_du_mois': row[0], 'nombre_de_commandes': row[1]} for row in data]

        return jsonify(data)
    


@app.route('/cuisine')
def cuisine():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = FALSE AND cuisine = 0 AND CONVERT(date_commande, DATE) =%s',(current_date,))
    cuisines = cursor.fetchall()
    cursor.close()
    return  render_template('cuisine.html', cuisines=cuisines)


@app.route('/cuisine/<id>', methods=['POST', 'GET'])
def updateCuisine(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE commande SET cuisine  = 1 WHERE id_commande = %s', (id,))
    mysql.connection.commit()
    
    socketio.emit('cuisine')

    return redirect(url_for('cuisine'))


@app.route('/menu_employe')
def menu_employe():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu')
    data = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tables_restaurant')
    tables = cursor.fetchall()
    cursor.close()
    return render_template('menu_employe.html', menus=data, tables=tables)


@app.route('/profile_employe')
def profile_employe():
    return render_template('profile_employe.html')


@app.route('/reservation')
def reservation():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu')
    menu = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    cursor.close()
    return render_template('reservation.html', menu=menu, categories=categories)

@app.route('/enregistrer_reservation')
def afficherR():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM employe WHERE acces = "employe"')
    employees = cursor.fetchall()
    cursor.close()

    return render_template('enregistrer_reservation.html', employees=employees)


@app.route('/enregistrer_reservation', methods=['GET', 'POST'])
def enregistrer_reservation():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        telephone = request.form['telephone']
        date_reservation = request.form['date']
        nbr_personne = request.form['nbrpersonne']
        heure_reservation = request.form['heure']
        employe = request.form['employe']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT nom_employe FROM employe WHERE matricule_employe  = %s', (employe,))
        reel_nom = cursor.fetchone()[0]
        cursor.close()

        # pdf = PDF(format='A3')
        pdf = PDF(format=(150, 220)) 
                # Créer un objet PDF

        # pdf = PDF(format='A3')
        pdf.add_page()

        # Entête de la facture
        # pdf.chapter_title('Informations du client:')
        # pdf.cell(0, 10, f'Nom du client: {name}', 0, 1)
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        pdf.set_font('Helvetica', 'BI', 10)
        pdf.multi_cell(0, 10, f'Date d\'emission: {formatted_time}', align='R')
        pdf.multi_cell(0, 10, f"Serveur: {reel_nom}", align='R')
        pdf.ln(5)

        # Tableau des articles commandés
        pdf.chapter_title('Information de reservation:')
        pdf.set_font('Helvetica', 'BI', 10)
        pdf.cell(55, 10, 'Nom client', 1)
        pdf.cell(40, 10, 'Numero de telephone', 1)
        pdf.cell(40, 10, 'Nombre de personne', 1)
        pdf.ln()
        pdf.set_text_color(0, 0, 255)
        pdf.set_font('Helvetica', 'BI', 10)
        pdf.cell(55, 10,nom+' '+prenom , 1)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(40, 10, str(telephone), 1)
        pdf.cell(40, 10, str(nbr_personne), 1)
        pdf.ln()

        # Résumé financier
        pdf.set_font('Arial', 'I', 9)
        pdf.chapter_title('Horaire:')
        pdf.cell(0, 10, 'Date reservation: '+str(date_reservation), 0, 1, 'R')
        pdf.cell(0, 10, 'Heure: ' + str(heure_reservation), 0, 1, 'R')
        # pdf.output("output.pdf")
        pdf_file = 'reservation' + nom + '_' + str(random.randint(1000, 9999))+'.pdf'
        # pdf_filename = os.path.join("application/static/reservation/", pdf_file)
        pdf_filename = os.path.abspath(os.path.join("application/static/reservation", pdf_file))
        pdf.output(pdf_filename)

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO reservation(nom, prenom, email, telephone, date_reservation, nbr_personne, heure_reservation, matricule_employe, date_reception, statut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (nom, prenom, email, telephone, date_reservation, nbr_personne, datetime.time.fromisoformat(heure_reservation), employe, current_date, 0))
        
        mysql.connection.commit()
        socketio.emit('connection')

            # Proposez le téléchargement du fichier PDF généré
        # return send_file(pdf_filename, as_attachment=True), 
        return send_file(pdf_filename, as_attachment=True, download_name='recu_reservation.pdf')

    return render_template('enregistrer_reservation.html')


@app.route('/hist_reservation')
def hist_reservation():

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM reservation WHERE statut = 1 AND matricule_employe = %s AND date_reception =%s',(session['matricule_employe'], current_date))
    reservation_terminer = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM reservation WHERE statut = 0 AND matricule_employe = %s AND date_reception =%s',(session['matricule_employe'], current_date))
    reservation_non_terminer = cursor.fetchall()
    cursor.close()
    return render_template('hist_reservation_employe.html', reservation_terminer=reservation_terminer, reservation_non_terminer=reservation_non_terminer)

@app.route('/hist_reservation/<id>', methods=['POST', 'GET'])
def UpdateReservation(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE reservation SET statut  = 1 WHERE id_reservation = %s', (id,))
    mysql.connection.commit()

    if session['acces'] == 'employe':
        return redirect(url_for("hist_reservation"))
    else :
        return redirect(url_for("commande_admin"))
    

@app.route('/hist_reservation_admin')
def hist_reservation_admin(): 
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM reservation WHERE statut = 1 AND date_reception =%s',(current_date,))
    reservation_terminer = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM reservation WHERE statut = 0 AND date_reception =%s',(current_date,))
    reservation_non_terminer = cursor.fetchall()
    cursor.close()
    return render_template('hist_reservation_admin.html', reservation_terminer=reservation_terminer, reservation_non_terminer=reservation_non_terminer)


@app.route('/reporting')
def reportingA():
    return render_template('reporting.html')


@app.route('/reporting', methods=['GET', 'POST'])
def reporting():
    if request.method == 'POST':
        date_debut = request.form['date_debut']
        date_fin = request.form['date_fin']
        cursor = mysql.connection.cursor()
        
        # Sélectionner les ventes entre date_debut et date_fin
        cursor.execute('SELECT COUNT(*) FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE) BETWEEN %s AND %s', (date_debut, date_fin))
        ventes = cursor.fetchone()[0]

        # Calculer le chiffre d'affaires entre date_debut et date_fin
        cursor.execute('SELECT SUM(total_commande) AS somme_totale FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE) BETWEEN %s AND %s', (date_debut, date_fin))
        chiffre_affaire = cursor.fetchone()[0]

        # Sélectionner les réservations terminées entre date_debut et date_fin
        cursor.execute('SELECT * FROM reservation WHERE statut = 1 AND date_reception BETWEEN %s AND %s', (date_debut, date_fin))
        reservation_terminer = cursor.fetchall()

        # Sélectionner les commandes terminées entre date_debut et date_fin
        cursor.execute('SELECT * FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE) BETWEEN %s AND %s', (date_debut, date_fin))
        terminees = cursor.fetchall()
        cursor.close()

        return render_template('reporting.html', ventes=ventes, terminees=terminees, reservation_terminer=reservation_terminer, chiffre_affaire=chiffre_affaire, date_debut=date_debut, date_fin=date_fin)
    



# MODIFICATION
@app.route('/get_table_info', methods=['GET', 'POST'])
def get_table_info():
    table_infos = request.json.get('idProprietes')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tables_restaurant WHERE id_table = %s", (table_infos,))
    donnees_tables = cursor.fetchone()
    donnees_tables = {
        'id_table': donnees_tables[0],
        'numero_table': donnees_tables[1],
        'nombre_place': donnees_tables[2],
        'occupe': donnees_tables[3],
    }   
    return jsonify(donnees_tables)

@app.route('/get_menu_info', methods=['GET', 'POST'])
def get_menu_info():
    menu_info = request.json.get('idProprietes')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM menu WHERE id_menu = %s", (menu_info,))
    donnees_menu = cursor.fetchone()
    donnees_menu = {
        'id_menu': donnees_menu[0],
        'nom_plat': donnees_menu[1],
        'prix': donnees_menu[2],
        'image': donnees_menu[3],
        'categories': donnees_menu[4],
    }   
    return jsonify(donnees_menu)


# PREDICTION
@app.route('/get_predict', methods=['GET', 'POST'])
def get_predict():
    mois = request.json.get('mois')
    jour = request.json.get('jour')

    predict_donnee = pd.DataFrame({'mois': [mois], 
                                    'jour': [jour]})
        
    chemin_modele = "application\static\GradientBRCommande.sav"
    model = joblib.load(chemin_modele)
    predict_commande = model.predict(predict_donnee)[0]

    prediction = {
        'prediction': int(predict_commande),

    }   
    return jsonify(prediction)
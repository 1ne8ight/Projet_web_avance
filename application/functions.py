import datetime
from flask_mysqldb import MySQL
import MySQLdb.cursors
from application import app
from application.config import Config_bdd


app.config.from_object(Config_bdd)
mysql = MySQL(app)
current_date = str(datetime.date.today())

def getByID(id, tablename):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM %s WHERE id = %s", (id, tablename))
    data = cursor.fetchone()
    cursor.close()
    return data

def getEmployeByEmail(email):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM employe WHERE email_employe = %s', (email,))
    data = cursor.fetchone()
    cursor.close()
    return data

def getCommandeCountByDate(date):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM commande WHERE CONVERT(date_commande, DATE)=%s', (date,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count

def getAllEmploye(acces):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM employe WHERE acces = %s', (acces,))
    data = cursor.fetchall()
    cursor.close()
    return data

#############***************TABLE************###################
def getTable():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tables_restaurant')
    data = cursor.fetchall()
    cursor.close()
    return data

def insertTable(numero_table, nombre_place):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tables_restaurant(numero_table, nombre_place) VALUES (%s, %s)", 
                       (numero_table, nombre_place))        
    mysql.connection.commit()

def deleteTable(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tables_restaurant WHERE id_table = %s', (id))
    mysql.connection.commit()


#############***************MENU************###################
def getMenu():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM menu')
    data = cursor.fetchall()
    cursor.close()
    return data

def insertMENU(nom_plat, prix):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO menu(nom_plat, prix) VALUES (%s, %s)", 
                       (nom_plat, prix))
    mysql.connection.commit()

def deleteMenu(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM menu WHERE id_menu = %s', (id))
    mysql.connection.commit()


#############***************COMMANDES************###################
def getCommandeTermine():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = TRUE AND CONVERT(date_commande, DATE) =%s',(current_date,))
    commande_terminer = cursor.fetchall()
    cursor.close()
    return commande_terminer

def getCommandeNonTermine():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM commande WHERE statuts = FALSE AND CONVERT(date_commande, DATE) =%s',(current_date,))
    commande_non_terminer = cursor.fetchall()
    cursor.close()
    return commande_non_terminer


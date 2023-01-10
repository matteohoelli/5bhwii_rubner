import mysql.connector
from flask import Flask
from flask_restful import Api, Resource

ssp_db = mysql.connector.connect(host="localhost", user="root", password="", database="ssp_db")

my_cursor = ssp_db.cursor()
my_cursor.execute("SELECT * FROM stats")

if (len(my_cursor.fetchall()) < 2):
    sql_player_first = f'INSERT INTO stats VALUES ("player", 0, 0, 0, 0, 0, 0)'
    sql_computer_first = f'INSERT INTO stats VALUES ("computer", 0, 0, 0, 0, 0, 0)'
    my_cursor.execute(sql_player_first)
    my_cursor.execute(sql_computer_first)
    ssp_db.commit()


def daten_speichern(symbol_anzhal_spieler, symbol_anzahl_computer, spieler_gwinnt, computer_gwinnt, gewonnen,
                    gewonnen_computer):
    auswahl_spieler = data_from_db(gewonnen, gewonnen_computer, spieler_gwinnt, computer_gwinnt)[0]
    auswahl_computer = data_from_db(gewonnen, gewonnen_computer, spieler_gwinnt, computer_gwinnt)[1]

    sql_spieler = f'UPDATE stats SET {gewonnen} = {auswahl_spieler} + {symbol_anzhal_spieler[gewonnen]}, wins = {spieler_gwinnt} WHERE name = "player"'
    sql_computer = f'UPDATE stats SET {gewonnen_computer} = {auswahl_computer} + {symbol_anzahl_computer[gewonnen_computer]}, wins = {computer_gwinnt} WHERE name = "computer"'

    my_cursor.execute(sql_spieler)
    my_cursor.execute(sql_computer)

    ssp_db.commit()


def data_from_db(gewonnen, gewonnen_computer, spieler_gewinnt, computer_gewinnt):
    my_cursor.execute(f'SELECT {gewonnen} FROM stats where name = "player"')
    auswahl_spieler = [int(record[0]) for record in my_cursor.fetchall()]
    auswahl_spieler = auswahl_spieler[0]
    my_cursor.execute(f'SELECT {gewonnen_computer} FROM stats where name = "computer"')
    auswahl_computer = [int(record[0]) for record in my_cursor.fetchall()]
    auswahl_computer = auswahl_computer[0]
    my_cursor.execute(f'SELECT wins FROM stats where name = "player"')
    gewinne_spieler = [int(record[0]) for record in my_cursor.fetchall()]
    gewinne_spieler = gewinne_spieler[0]
    my_cursor.execute(f'SELECT wins FROM stats where name = "computer"')
    gewinne_computer = [int(record[0]) for record in my_cursor.fetchall()]
    gewinne_computer = gewinne_computer[0]
    spieler_gewinnt = gewinne_spieler + spieler_gewinnt
    computer_gewinnt = gewinne_computer + computer_gewinnt

    return auswahl_spieler, auswahl_computer, spieler_gewinnt, computer_gewinnt


def reset_db():
    sql_player_clear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "player"'
    sql_computer_clear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "computer"'
    my_cursor.execute(sql_player_clear)
    my_cursor.execute(sql_computer_clear)
    ssp_db.commit()


def show_all_data():
    my_cursor.execute("SELECT * FROM stats")
    ergebnis = my_cursor.fetchall()
    data_spieler = {"name": ergebnis[0][0], "stein": ergebnis[0][1], "spock": ergebnis[0][2], "papier": ergebnis[0][3],
                    "echse": ergebnis[0][4], "schere": ergebnis[0][5], "wins": ergebnis[0][6]}
    data_computer = {"name": ergebnis[1][0], "stein": ergebnis[1][1], "spock": ergebnis[1][2], "papier": ergebnis[1][3],
                     "echse": ergebnis[1][4], "schere": ergebnis[1][5], "wins": ergebnis[1][6]}
    print(data_spieler)
    print(data_computer)
    return data_spieler


app = Flask(__name__)
api = Api(app)


class ApiClass(Resource):
    def get(self):
        data = show_all_data()
        return data


api.add_resource(ApiClass, '/')
app.run(debug="True")

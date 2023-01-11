import random

from server import data_from_db, reset_db, daten_speichern, show_all_data

symbol_dictionary = {"stein": 1, "spock": 2, "papier": 3, "echse": 4, "schere": 5}
dictionary_symbol = {1: "stein", 2: "spock", 3: "papier", 4: "echse", 5: "schere"}
count_symbol_player = {"stein": 0, "spock": 0, "papier": 0, "echse": 0, "schere": 0}
count_symbol_computer = count_symbol_player.copy()
spieler_gewonnen_mit = []

print("Servus, viel spass bei Schere, Stein, Papier, Spock, Echse!")


def menu():
    exit = False
    print("Willkommen im Menü!")
    while exit == False:
        todo = input("Sie können wählen zwischen /spiel, /resetdb, /stats oder /exit: ")
        if todo == "/spiel":
            spiel()
        elif todo == "/resetdb":
            reset_db()
        elif todo == "/stats":
            show_all_data()
        elif todo == "/exit":
            exit = True


def spiel():
    spielmodus = "E"
    runden_zaehler = 0
    next_round = "j"
    while next_round == "j":
        spieler_gewinnt = 0
        computer_gewinnt = 0
        runden_zaehler += 1

        if (runden_zaehler > 5):
            spielmodus = input(
                "\nHaben dir die Runden gefallen und du willst nochmal spielen? Wenn ja, soll die nächste Runde Leicht(E) oder Hart(H) sein?: ")
        ausgewaehlt = input("\nNimmst du Schere, Stein, Papier, Spock oder Echse? : ")
        if ausgewaehlt not in symbol_dictionary:
            print("Falsche Eingabe, nochmal eingeben!")
            continue
        count_symbol_player[ausgewaehlt] = 1
        ausgewaehlt_zahl = symbol_dictionary[ausgewaehlt]
        print("\nSpieler:", ausgewaehlt)

        if spielmodus == "E":
            ausgewaehlt_computer2 = random.randrange(1, len(symbol_dictionary) + 1)
            ausgewaehlt_computer = dictionary_symbol[ausgewaehlt_computer2]
            count_symbol_computer[ausgewaehlt_computer] = 1
            print("\nComputer:", dictionary_symbol[ausgewaehlt_computer2], "\n")
        elif spielmodus == "H":
            zaehler = 0
            element = spieler_gewonnen_mit[0]
            for i in spieler_gewonnen_mit:
                haeufigkeit_now = spieler_gewonnen_mit.count(i)
                if (haeufigkeit_now > zaehler):
                    zaehler = haeufigkeit_now
                    element = i
            if (element == "echse" or element == "schere"):
                ausgewaehlt_computer2 = 1
            elif (element == "stein"):
                ausgewaehlt_computer2 = 2
            elif (element == "spock"):
                ausgewaehlt_computer2 = 3
            elif (element == "papier"):
                ausgewaehlt_computer2 = 4

        unterschied = (ausgewaehlt_zahl - ausgewaehlt_computer2) % 5
        if unterschied == 0:
            gewinner = "Unentschieden!"
        elif unterschied <= 2:
            gewinner = "Spieler gwinnt!"
            spieler_gewonnen_mit.append(ausgewaehlt)
            spieler_gewinnt += 1
        elif unterschied <= 4:
            gewinner = "Computer gwinnt!"
            computer_gewinnt += 1

        spieler_gewinnt = data_from_db(ausgewaehlt, ausgewaehlt_computer, spieler_gewinnt, computer_gewinnt)[2]
        computer_gewinnt = data_from_db(ausgewaehlt, ausgewaehlt_computer, spieler_gewinnt, computer_gewinnt)[3]

        daten_speichern(count_symbol_player, count_symbol_computer, spieler_gewinnt, computer_gewinnt, ausgewaehlt,
                        ausgewaehlt_computer)
        print(gewinner)
        print("\nSpieler:", spieler_gewinnt, "Computer:", computer_gewinnt)

        next_round = input("\nNoch eine Runde?(j/n)")
        if next_round == "n":
            menu()


if __name__ == "__main__":
    menu()

import random

mlist = []
aufHand = []


def ziehung(anz=5):
    global mlist, aufHand
    mlist = []
    aufHand = []
    for i in range(0, 52):
        mlist.append(i)
    for j in range(anz):
        index = random.randrange(0, 52)
        lastposition = len(mlist) - 1 - j
        mlist[index], mlist[lastposition] = mlist[lastposition], mlist[index]
    for z in mlist[-anz:]:
        aufHand.append(z)
        mlist[mlist.index(z)] = card(z)
    return mlist[-anz:], aufHand


def card(zahl):
    symbol = getSymbol(zahl)
    if symbol == 0:
        symbol = 'Kreuz'
    elif symbol == 1:
        symbol = 'Pik'
    elif symbol == 2:
        symbol = 'Herz'
    else:
        symbol = 'Karo'

    nummer = getNumber(zahl)
    if nummer == 10:
        nummer = 'Bube'
    elif nummer == 11:
        nummer = 'Dame'
    elif nummer == 12:
        nummer = 'König'
    elif nummer + 1 == 1:
        nummer = 'Ass'
    else:
        nummer = nummer + 1

    return symbol + ' ' + str(nummer)


def getNumber(zahl):
    return zahl % 13


def getSymbol(zahl):
    return int(zahl) // 13


def getAufHand(aufHand):
    aufHand_new = []
    for i in range(len(aufHand)):
        aufHand_new.append(getNumber(aufHand[i]))
    return aufHand_new


def getSym(aufHand):
    sym = []
    for i in range(len(aufHand)):
        sym.append(getSymbol(aufHand[i]))
    return sym


def royal_flush(aufHand):
    aufHand_new = getAufHand(aufHand)
    sym = getSym(aufHand)
    counter = 0
    aufHand_new.sort()
    for j in range(len(aufHand)):
        if ((sym[j] - sym[j - 1]) != 0):
            return False
    for i in range(2, 5):
        if ((aufHand_new[0] == 0) and (aufHand_new[1] == 9) and ((aufHand_new[i] - aufHand_new[i - 1]) == 1)):
            counter += 1
    if (counter == 3):
        return True
    return False


def Straße_flush(aufHand):
    aufHand_new = getAufHand(aufHand)
    sym = getSym(aufHand)
    counter = 0
    aufHand_new.sort()
    for j in range(len(aufHand)):
        if ((sym[j] - sym[j - 1]) != 0):
            return False
    for i in range(len(aufHand)):
        if (((aufHand_new[i] - aufHand_new[i - 1]) == 1)):
            counter += 1
    if (counter == 4):
        return True
    return False


def vierling(aufHand):
    aufHand_new = getAufHand(aufHand)
    dup = [x for i, x in enumerate(aufHand_new) if i != aufHand_new.index(x)]
    dup.append("fill")
    counter = 0
    for j in range(len(aufHand)):
        if ((len(dup) == 4)):
            if (dup[0] == aufHand_new[j]):
                counter += 1
    if (counter == 4):
        return True
    return False


def full_house(aufHand):
    aufHand_new = getAufHand(aufHand)
    aufHand_new.sort()
    if ((drilling(aufHand_new[0:3]) and pair(aufHand_new[3:5])) or (
            pair(aufHand_new[0:2]) and drilling(aufHand_new[2:5]))):
        return True
    return False


def flush(aufHand):
    sym = getSym(aufHand)
    counter = 0
    for i in range(len(aufHand)):
        if ((sym[i] - sym[i - 1]) == 0):
            counter += 1
    if (counter >= 4):
        return True
    return False


def Straße(aufHand):
    aufHand_new = getAufHand(aufHand)
    counter = 0
    aufHand_new.sort()
    for i in range(len(aufHand)):
        if ((aufHand_new[i] - aufHand_new[i - 1]) == 1):
            counter += 1
    if (counter >= 4):
        return True
    return False


def drilling(aufHand):
    aufHand_new = getAufHand(aufHand)
    dup = [x for i, x in enumerate(aufHand_new) if i != aufHand_new.index(x)]
    dup.append("fill")
    counter = 0
    for j in range(len(aufHand)):
        if ((len(dup) == 1) or (dup[0] == dup[1])):
            if (dup[0] == aufHand_new[j]):
                counter += 1
    if (counter == 3):
        return True
    return False


def twopair(aufHand):
    aufHand_new = getAufHand(aufHand)
    dup = [x for i, x in enumerate(aufHand_new) if i != aufHand_new.index(x)]
    dup.append("fill")
    if ((len(dup) == 3) and (dup[0] != dup[1])):
        return True
    return False


def pair(aufHand):
    aufHand_new = getAufHand(aufHand)
    dup = [x for i, x in enumerate(aufHand_new) if i != aufHand_new.index(x)]
    if (len(dup) == 1):
        return True
    return False


dic = {}
kombi = ['Royal Flush', 'Straße Flush', 'Vierling', 'Full House', 'Flush', 'Straße', 'Drilling', 'Two Pair', 'Pair',
         'High Card']


def createdic(min, max):
    for i in range(min, max + 1):
        dic[i] = 0


def kombis(aufHand):
    for i in range(len(aufHand)):
        if royal_flush(aufHand):
            dic[0] += 1
            return 'Royal flush'
        elif Straße_flush(aufHand):
            dic[1] += 1
            return 'Straße flush'
        elif vierling(aufHand):
            dic[2] += 1
            return 'Four of a kind'
        elif full_house(aufHand):
            dic[3] += 1
            return 'Full House'
        elif flush(aufHand):
            dic[4] += 1
            return 'Flush'
        elif Straße(aufHand):
            dic[5] += 1
            return 'Straße'
        elif drilling(aufHand):
            dic[6] += 1
            return 'Three of a kind'
        elif twopair(aufHand):
            dic[7] += 1
            return 'Two pair'
        elif pair(aufHand):
            dic[8] += 1
            return 'Pair'
    dic[9] += 1
    return "High Card"


def kalkulation(anz):
    for j in range(anz):
        ziehung()
        kombis(aufHand)
    return dic


def kalkAusgabe(dic, kombi, anz):
    ausgabe = 0
    for i in range(0, 10):
        print(kombi[i] + " : " + str(round((dic[i] / anz) * 100, 5)) + "%")
    return ausgabe


if __name__ == '__main__':
    createdic(0, 9)
    kalkulation(100000)
    print(dic)
    kalkAusgabe(dic, kombi, 100000)


def formatovani (rodne_cislo):
    "zjistuji spravnost formatu RC, počet cisel, umisteni lomitka"
    vysledek = True
    delka = len(cislo) 

    for x in range(len(cislo)):
        if x!=6 and cislo[x].isdigit() != True:
            vysledek = False
        if x==6 and cislo[x] != '/':
            vysledek = False
    if delka == 11 and vysledek == True:
        return True
    else:
        return False

def delitelnost(rodne_cislo):
    "Zjistuji delistelnost 11"
    cislo.remove('/')
    cislo2 = int(''.join(cislo))
    if cislo2 % 11 == 0:
        return True
    else:
        return False

def datum (rodne_cislo):
    "Generuje datum narozeni z RC"
    den = int(''.join(cislo[4:6]))
    mesic0 = int(''.join(cislo[2:4]))
    if mesic0 > 12:
        mesic = mesic0 - 50
    else:
        mesic = mesic0
    rok = int(''.join(cislo[0:2])) + 1900
    return 'Datum narozeni: {}.{}.{}'.format(den,mesic, rok)

def pohlavi (rodne_cislo):
    "Generuje pohlaví z RC"
    mesic0 = int(''.join(cislo[2:4]))
    if mesic0 > 12:
        return'Pohlaví: žena'
    else:
        return 'Pohlaví: muž'


cislo = list(input('Napište rodné číslo:'))
while True:
    if formatovani(cislo) == True and delitelnost(cislo) == True:
        print (datum(cislo)) 
        print (pohlavi(cislo))
        break
    else :
        cislo = list(input("""
Takové rodné číslo neexistuje!
Rodné číslo pište ve formatu 123456/1234: """))

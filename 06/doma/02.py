#uzivatel zada rodne cislo, program vypise, zdali jej zadal ve spravnem formatu a vypise zjistitelne informace

rodne_cislo = list(input('Napište rodné číslo:'))

vysledecek = True
delka = len(rodne_cislo) #delka musi byt 11

for x in range(len(rodne_cislo)): #zjistuji spravný format
    if x!=6 and rodne_cislo[x].isdigit() != True:
        vysledecek = False
    if x==6 and rodne_cislo[x] != '/':
        vysledecek = False

rodne_cislo.remove('/') #pripravuji na zajisteni podminky delitenosti 11
rodne_cislo2 = int(''.join(rodne_cislo))

while True: 
    if vysledecek == True and rodne_cislo2 % 11 == 0 and delka == 11: #plati vsecny podminky, vypisuje vysledek
        den = ''.join(rodne_cislo[4:6])
        mesic0 = int(''.join(rodne_cislo[2:4]))
        if mesic0 > 12:
            print ("""
Pohlaví: žena""")
            mesic = mesic0 - 50
        else:
            print ("""
Pohlaví: muž""")
            mesic = mesic0
        rok = int(''.join(rodne_cislo[0:2])) + 1900
        print('Datum narozeni je: {}.{}.{}'.format(den,mesic, rok))
        break
    else: #neplati vsechny podminky, opakuje kontrolu podminek
        rodne_cislo = list(input("""
Takové rodné číslo neexistuje!
Rodné číslo pište ve formatu 123456/1234: """))
        vysledecek = True
        delka = len(rodne_cislo)

        for x in range(len(rodne_cislo)):
            if x!=6 and rodne_cislo[x].isdigit() != True:
                vysledecek = False
            if x==6 and rodne_cislo[x] != '/':
                vysledecek = False

        rodne_cislo.remove('/')
        rodne_cislo2 = int(''.join(rodne_cislo))

from random import randrange

def vyhodnot (retezec):
    if 'xxx' in retezec:
        return "x"
    if 'ooo' in retezec:
        return "o"
    elif '-' not in retezec:
        return "!"
    else:
        return "-"
    
def tah(retezec, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    pozice_policka = int(cislo_policka)
    novy_retezec = retezec[:(pozice_policka-1)] + symbol + retezec[pozice_policka:]
    return novy_retezec

def tah_hrace(retezec, cislo_policka):
    "vrati pole se zmenou dle tahu hrace"
    while True:
        if cislo_policka.isdigit():
            pozice_policka = int(cislo_policka)
            if pozice_policka >= 1 and pozice_policka <= 20:
                if retezec[(pozice_policka-1)] == '-':
                    novy_retezec = retezec[:(pozice_policka-1)] + 'x' + retezec[pozice_policka:]
                    return novy_retezec
                else:
                    cislo_policka = input('Pozice musi byt dosud neobsazená: ')
            else:
                cislo_policka = input('Pozice musi byt cislo od 1 do 20: ')    
        else:
            cislo_policka = input('Pozice musi byt cislo: ')

def tah_pocitace(retezec, pozice_policka):
    "vrati pole se zmenou dle tahu pocitace-nahodny tah"
    while True:
        if retezec[(pozice_policka-1)] == '-':
            novy_retezec = retezec[:(pozice_policka-1)] + 'o' + retezec[pozice_policka:]
            return novy_retezec
        else:
            pozice_policka = randrange(1, 21)
            

def piskvorky1d(retezec):
    while True:
        if vyhodnot(retezec) == '-':
            retezec_hrac = tah_hrace(retezec, input('Zadej pozici, na kterou chces tahnout: '))
            print(retezec_hrac)
            if vyhodnot(retezec_hrac) == '-':
                retezec_pocitac = tah_pocitace(retezec_hrac, randrange(1, 21))
                print(retezec_pocitac)
                retezec = retezec_pocitac
            else:
                return vyhodnot(retezec_hrac)
        else:
            return vyhodnot(retezec)

#print(vyhodnot(input('napis rezetec:')))
#print(tah('--------------------', input('Napis pozici: '), input('napis symbol: ')))
#print(tah_hrace('--------------------', input('Napis pozici: ')))
#print(tah_pocitace('--------------------',randrange(1, 21)))
print(piskvorky1d('--------------------'))
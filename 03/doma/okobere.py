
from random import randrange

body = 0
odpoved = input ('Vítej ve hře "Oko bere"! Účelem hry je získat 21 bodů. Nesmíš ovšem získat více, pokud se tak stane, hra končí. Tvé skóre je 0. Chceš hrát? ano/ne: ')

while odpoved == 'ano':
    tah_pocitace = randrange(2,11)
    print(tah_pocitace)
    body = body + tah_pocitace
    if body > 21:
        print ('Ajaj! Získal/a jsi:', body,'Prohrál/a jsi! Konec hry!')
        quit()
    elif body == 21:
        print ('Jsi vítěz. Gratuluji!')
        quit()
    else:
        print('Tvé skóre je:', body)
    odpoved = input('Chceš pokračovat ve hře? ano/ne: ')

if odpoved == 'ne':
    print('Chybí odvaha, co? Konec hry!')
    quit()
else :
    print('Omlouvám se, nerozumím. Konec hry!')
    quit()
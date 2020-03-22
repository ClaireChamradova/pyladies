prvnicislo = int(input('Zadej číslo: '))
operace = input('Zadej znaménko matematické operace: ')
druhecislo = int(input('Zadej druhé číslo: '))

if operace == '+':
    vysledek = '{} + {} je {}.'.format(prvnicislo, druhecislo, prvnicislo
    +druhecislo)
elif operace == '*':
    vysledek = '{} * {} je {}.'.format(prvnicislo, druhecislo, prvnicislo
    *druhecislo)
elif operace == '-':
    vysledek = '{} - {} je {}.'.format(prvnicislo, druhecislo, prvnicislo
    -druhecislo)
elif operace == '/' or ':':
    vysledek = '{} / {} je {}.'.format(prvnicislo, druhecislo, prvnicislo
    /druhecislo)
else:
    print('Nerozumím.')

print (vysledek)
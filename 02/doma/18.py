# Tento program rozdává naivní rady do života a má vnořené ify.

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')


if stastna_retezec != 'ano' and stastna_retezec != 'ne':
    print('Nerozumím!')
    exit ()

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    if stastna_retezec == 'ano':
        print('Gratuluji!')
    elif stastna_retezec == 'ne':
        print ('Zkus míň utrácet.')
elif bohata_retezec == 'ne':
    if stastna_retezec == 'ano':
        print('Zkus se víc usmívat!')
    elif stastna_retezec == 'ne':
        print ('To je mi líto.')
else:
    print('Nerozumím!')
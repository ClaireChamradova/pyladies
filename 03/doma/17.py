
prvnicislo = int(input ('Zadej číslo: '))
cislo = prvnicislo

for dalsicisla in range(4):
    dalsicislo = int(input ('Zadej číslo: '))
    if dalsicislo < cislo:
        cislo = dalsicislo

print ('Nejmenší zadané číslo je:', cislo)
from random import randrange

cislo = 0
do = 100

while cislo <= do:
    zbytek = cislo % 2
    if zbytek != 1:
        print(cislo)
    cislo = cislo + 1

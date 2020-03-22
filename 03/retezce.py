#retezec = 'Ahoj'
#print (retezec.upper())
#print (retezec.lower())

#jmeno = input('Jaké je tvé křestní jméno? ')
#prijmeni = input('Jaké je tvé příjmení? ')
#print ('Tvé iniciály jsou:', jmeno[0].upper() + prijmeni[0].upper())

#retezec = 'cokolada'
#kousek = retezec[5:]
#print(kousek)

stary_retezec = input ('Zadej libovolné slovo: ')
pozice = int(input ('Zadej pozici, kterou chceš vyměnit: '))
nove = stary_retezec[pozice-1]
print('Písmeno, které chceš vyměnit je :', nove)
znak = input ('Zadej nový znak: ')
novy_retezec = stary_retezec[:(pozice-1)] + znak + stary_retezec[pozice:]
print('Nové slovo je: ', novy_retezec)


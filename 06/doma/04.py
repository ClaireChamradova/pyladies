
zviratka = {'Arya': 'králík','Fia': 'pes','Terka': 'ovce','Bublina': 'kočka'}

for jmeno, mazlicek in zviratka.items():
    print ('{} je boží {}!'.format(jmeno, mazlicek))
print("""
""")

zviratka['Bobek'] = 'morče'

for jmeno, mazlicek in zviratka.items():
    print ('{} je boží {}!'.format(jmeno, mazlicek))
print("""
""")

del zviratka['Fia']

for jmeno, mazlicek in zviratka.items():
    print ('{} je boží {}!'.format(jmeno, mazlicek))


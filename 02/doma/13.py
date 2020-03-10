nohy = int(input('Kolik máš nohou?'))

if nohy >= 100:
    print ('Zdravím tě stonožko!')
elif nohy >= 50:
    print ('To musí být útrata v obuvi!')
elif nohy > 6:
    print ('Tvoje rohožka musí trpět..')
elif nohy == 6:
    print ('Pavouci jsou cool!')
elif nohy > 4:
    print ('Chudáčku pavoučku, kdo ti utrhl nožičku?')
elif nohy == 4:
    print ('To se to běhá, co?')
elif nohy == 3:
    print ('Divný počet!')
elif nohy == 2:
    print ('Moc normální. S tebou musí být nuda.. Pokud teda nemáš křídla!')
elif nohy > 0:
    print ('Aj! :(')
else:
    print ('Tak to jsi pak housenka? Nebo ryba?')
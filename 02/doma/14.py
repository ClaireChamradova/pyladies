tajne_heslo = input ('Zadej tajné heslo: ')

if tajne_heslo == 'kralik':
    print ('Správně! Tak já ti prozradím tajemství. Mám jednoho doma. Má zbarvení jako border kolie a jemenuje se Arya.')
elif tajne_heslo != 'kralik':
    napoveda = input ('Špatně! Chceš nápovědu? ano/ne: ')
    if napoveda == 'ano':
        druhy_pokus = input ('Je to zvíře, které má velké uši a hopská. Co je to? (piš bez malým a bez diakritiky): ')
        if druhy_pokus == 'kralik':
                print ('Správně! Tak já ti prozradím tajemství. Mám jednoho doma. Má zbarvení jako border kolie a jemenuje se Arya.')
        elif druhy_pokus != 'kralik':
            treti_pokus = input ('Těsně vedle! Zkus to druhé ušaté zvířátko: ')
            if treti_pokus == 'kralik':
                print ('No konečně! Tak já ti prozradím tajemství. Mám jednoho doma. Má zbarvení jako border kolie a jemenuje se Arya.')
    
    elif napoveda == 'ne':
        print ('Tak nic nebude.')
    else:
        print ('Špatná odpověď!')
        
        
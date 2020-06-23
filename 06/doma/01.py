
#serazeni seznamu podle druheho pismene slova

domaci_zvire = ['pes', 'kocka', 'kralik', 'had', 'andulka']
print(domaci_zvire)
new_list= []
domaci_zvire2 = []
domaci_zvire3 = []

for zvire in domaci_zvire: #rozdeleni na prvni pismeno a zbytek slova
    zvire.split()
    a = zvire[0]
    b = zvire [1:]
    new_list.append(b) #vytvoreni podseznamu
    new_list.append(a)
    domaci_zvire2.append(new_list)
    new_list = []

domaci_zvire2 = sorted(domaci_zvire2) #serazeni

for zvirata in domaci_zvire2: 
    zvire = zvirata[1] + zvirata[0] #spojeni zpet do celych slov
    domaci_zvire3.append(zvire)

print(domaci_zvire3)
#sifrovaci program

answer = input("""Hi! I am a CEASAR CIPHER PROGRAM! I can help with ciphering and deciphering of your text.
Would you like to CIPHER your text? yes/no: """)

if answer == 'yes': #chci zasifrovat
    plaintext = input('Write the text: ')
    key = input ('Choose a value of a key: ')

    while True: #aby byl klic vzdy cislo
        if key.isdigit():
            intkey = int(key)
            break
        else:
            key = input('The key has to be a digit:')

    print("""
plaintext:""", plaintext)
    print('key:', key)

    code = [ord(a) for a in plaintext] #zmena písmen na ciselne hodnoty ASCII
    recode = [] #pricteni hodnoty 
    ciphertext = [] #zasifrovany text
    for number in code:
        if number >= 65 and number <= 90: #definovani oblasti velkych pismen
            recode = (((number-65 + intkey)%26)+65)
            ciphertext.append(recode)
        elif number >= 97 and number <= 122:#definovani oblasti malych pismen
            recode = (((number-97 + intkey)%26)+97)
            ciphertext.append(recode)
        else :
            recode = number
            ciphertext.append(recode)

    print ('ciphertext:', ''.join([chr(c) for c in ciphertext])) #zmena ciselne hodnoty ASCII na pismena

if answer == 'no':
    answer2= input('Would you like to DECIPHER your text? yes/no: ')
    if answer2 == 'yes':
        plaintext = input('Write the text: ')
        key = input ('Choose a value of a key: ')

        while True:
            if key.isdigit():
                intkey = int(key)
                break
            else:
                key = input('The key has to be a digit:')

        print("""
plaintext:""", plaintext)
        print('key:', key)

        code = [ord(a) for a in plaintext]
        recode = []
        ciphertext = []
        for number in code:
            if number >= 65 and number <= 90:
                recode = (((number-65 - intkey)%26)+65)
                ciphertext.append(recode)
            elif number >= 97 and number <= 122:
                recode = (((number-97 - intkey)%26)+97)
                ciphertext.append(recode)
            else :
                recode = number
                ciphertext.append(recode)
        print ('ciphertext:', ''.join([chr(c) for c in ciphertext]))
    
    if answer2 != 'yes' and answer2 != 'no':
        print ("I'm sorry! I can't help!")

if answer != 'yes' and answer != 'no':
    print ("I'm sorry! I can't help!")

print ('Have a nice day!')
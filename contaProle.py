conteggio ={}
punteggiatura = ['?','@','!','"','£','%','&','/','(',')','=','^','|','$','+','-','*',',']
parola_dig = input('Inserisci una frase a piacere\n')

# trasformo l'input stringa in una lista ordinata
parola = parola_dig.lower()
for punto in punteggiatura:
    parola=parola.replace(punto,'')

#prendo le vocali uniche
parola_list = parola.split(' ')
parola_list_un = set(parola_list)

#per ogni vocale unica confronto ogni vocale presente nella lista creata dalla stringa
print('Il risultato è il seguente:')
for vocale in parola_list_un:
    count = 0
    for vocale_cerca in parola_list:
        if vocale_cerca == vocale:
            count +=1
        #a fine ciclo creo un campo per ogni vocale unica a cui assegno il valore della ripetizione
        conteggio[vocale] = count
    print(f'La lettera {vocale} è ripetuta {count}')

print(f'Riasumendo abbiamo:\n{conteggio}')
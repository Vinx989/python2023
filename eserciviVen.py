conteggio ={}

parola_dig = input('Inserisci una parola a piacere\n')

# trasformo l'input stringa in una lista
parola = parola_dig.lower()
parola_lista = list(parola)

#prendo le vocali uniche
parola_list_un = set(parola_lista)

#per ogni vocale unica confronto ogni vocale presente nella lista creata dalla stringa
for vocale in parola_list_un:
    count = 0
    for vocale_cerca in parola_lista:
        if vocale_cerca == vocale:
            count +=1
        #a fine ciclo creo un campo per ogni vocale unica a cui assegno il valore della ripetizione
        conteggio[vocale] = count

print(conteggio)

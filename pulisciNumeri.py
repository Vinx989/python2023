# i numeri che mi servono per i controlli
numeri= ['0','1','2','3','4','5','6','7','8','9']
#flag per il ciclo while
split_on = True
#variabile che mi servirà come controllo
a = 0

numeri_unici= [] #lista vuota per i numeri unici(contenitore)

while split_on:
    numeri_dig = input('Inserisci una secuenza di numeri\n')

    lista_numeri= list(numeri_dig) #creo la lista di numeri

    #check se ha scritto qualcosa che non va
    for num in lista_numeri:
        if num not in numeri:
            print('Mi dispiace, la secuenza deve essere solo numerica\nRiprova!')
            a = num
            break
        else:
            #aggiungo in numero alla lista
            if int(num) not in numeri_unici:
                numeri_unici.append(int(num))

    # questo confronto serve per vedere se un valore è risultato essere un NON numero
    if a == 0:
        print(f'I numeri unici sono .\n{numeri_unici}')
        split_on = False
    else:
        split_on = True
        a = 0
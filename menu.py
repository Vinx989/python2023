menu_on = True
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',',','?','@','!','"','£','%','&','/','(',')','=','^','|','$','+','-','*']
operazioni = ['somma','sottrazione','moltiplicazione','divisione','i']

while menu_on:
    accedi = input('Benvenuto.\nPreim "Y" per fare una delle quattro operazioni, premi "N" per uscire\n')
    if accedi.lower() not in ['y','n']:
        print('Si prega di digitare correttamente')
    elif accedi.lower() == 'n':
        print('Grazie per averci visitato')
        menu_on = False
    else:
        operaz_on = True
        while operaz_on:
            scelta_operazione = input(f'Quali operazione vuoi fare?\n{operazioni[0]}, {operazioni[1]}, {operazioni[2]}, {operazioni[3]}\nDigita "I" per tornare al menù principale\n')
            if scelta_operazione.lower() not in operazioni:
                print('Digitare correttamente')
            elif scelta_operazione.lower() == 'i':
                operaz_on = False
            else:
                index = operazioni.index(scelta_operazione.lower())
                cifre_on =True
                while cifre_on:
                    cifra_11=(input('Inserisci il primo numero\n'))
                    cifra_22 =(input('Inserisci il secondo numero\n'))
                    check_1 = list(cifra_11)
                    check_2 = list(cifra_22)
                    if len(set(check_1) & set(alfabeto)) !=0 or len(set(check_2) & set(alfabeto)) !=0:
                        print('Si prega di inserire due numeri')
                    else:
                        cifra_1 = float(cifra_11)
                        cifra_2 = float(cifra_22)
                        if index == 0:
                            risultato = cifra_1+cifra_2
                            print(f'Il risultato è: {risultato}')
                        elif index == 1:
                            risultato = cifra_1-cifra_2
                            print(f'Il risultato è: {risultato}')
                        elif index == 2:
                            risultato = cifra_1*cifra_2
                            print(f'Il risultato è: {risultato}')
                        else:
                            #inserirecondizione per zero
                            if cifra_2==0.0:
                                print('Errore. Non puoi dividere per zero!')
                            else:
                                risultato = cifra_1/cifra_2
                                print(f'Il risultato è: {risultato}')
                        print('Proviamo ancora!')
                        cifre_on=False

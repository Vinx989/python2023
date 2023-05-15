# Piccolo programa che srve per il controllo vendite

# qui inizializiamo la variabile buleana che ci permetterà di uscire dal menu
# in più inseriamo una lista di numeri che ci seviranno per il controllo dell'input
# passo finale inizializziamo il menu delle vendite che sarà un dizionari di dizionari
menu_on = True
numeri= ['0','1','2','3','4','5','6','7','8','9']
oggetti_negozio = {'banana':{
                            'prezzo': 0.75,
                            'quantita': 5,
                            'totale_fat': 3.75}
}

#ogni item inserito sarà inserito come dizionario
singolo_item={}

while menu_on:
    print('Benvenuto!\nChe operazione vuoi fare?')
    scelta = input('Premi 1 per aggiungere un prodotto da vendere\nPremi 2 per controllo vendite\nPremi 3 per uscire dal programma\n')
    #questo if serve da controllo
    check = True
    if scelta not in ['1','2','3']:
        print('Si prega di digitare in modo corretto')
    elif scelta=='3':
        menu_on = False
    else:
        # qui iniziamo le nostre operazioni
        if scelta == '1':
            nome_prodotto = input('Iserire il nome prodotto:\n')
            if nome_prodotto not in oggetti_negozio:              # se l'oggetto non è nel menu allora lo aggiungiamo
                nuovo_on = True
                while nuovo_on:
                    nuovo_prezzo = input('Inserisci il prezzo:\n').replace(',','.').replace(' ','')
                    quantita_venduta= input('Quantità venduta:\n').replace(' ','')
                    nuovo_prezzo_check = list(nuovo_prezzo)
                    quantita_venduta_check = list(quantita_venduta)
                    print(quantita_venduta_check)
                    print(nuovo_prezzo_check)
                    for num in quantita_venduta_check:
                        if num not in numeri:
                            check = False
                    for num in nuovo_prezzo_check:
                        if num !='.' and num not in numeri:
                            check = False
                    if check != False:
                        quantita_venduta = int(quantita_venduta)
                        nuovo_prezzo = float(nuovo_prezzo)
                        singolo_item['prezzo']=nuovo_prezzo
                        singolo_item['quantita']= quantita_venduta
                        singolo_item['totale_fat']= quantita_venduta*nuovo_prezzo
                        oggetti_negozio[nome_prodotto]={}
                        oggetti_negozio[nome_prodotto]=singolo_item
                        singolo_item={}
                        nuovo_on = False
                    else:
                        print('Error. Digitare correttamente')
            elif nome_prodotto in oggetti_negozio:               #se l'oggetto è già presente allora vediamo cosa volgiamo
                caricamento_on = True                            #aggiornare
                while caricamento_on:
                    scelta_caricamento = input('Digita 1 per aggiornare la quantità\nDigita 2 per aggiornare il prezzo\n')
                    #controllo sulla scelta
                    if scelta_caricamento not in ['1','2']:
                        print('Si prega di digitare in modo corretto')
                    else:
                        # da qui in poi se si sbaglia a digitare allora darà errore
                        if scelta_caricamento == '1':
                            quantita_aggiorn=input(f'La quantità attuale è {oggetti_negozio[nome_prodotto]["quantita"]}, quanto ne vuoi aggiungere?\n')
                            quantita_aggiorn_check = list(quantita_aggiorn)
                            #controllo che il numero inserito sia intero
                            for num in quantita_aggiorn_check:
                                if num not in numeri:
                                    check = False
                            if check != False:
                                quantita_aggiorn = int(quantita_aggiorn)
                                oggetti_negozio[nome_prodotto]['quantita'] += quantita_aggiorn
                                oggetti_negozio[nome_prodotto]['totale_fat'] += quantita_aggiorn*oggetti_negozio[nome_prodotto]['prezzo']
                                caricamento_on = False
                            else:
                                print('Errore. Digitare correttamente')
                        if scelta_caricamento == '2':
                            # controllo che il numero inserito sia intero
                            prezzo_aggiorn = input(f'Il prezzo attuale è {oggetti_negozio[nome_prodotto]["prezzo"]}, quale è il nuovo prezzo?\n').replace(' ','').replace(',','.')
                            prezzo_aggiorn_check = list(prezzo_aggiorn)
                            for num in prezzo_aggiorn_check:
                                if num !='.' and num not in numeri:
                                    check = False
                            if check != False:
                                prezzo_aggiorn = float(prezzo_aggiorn)
                                oggetti_negozio[nome_prodotto]['prezzo'] = prezzo_aggiorn
                                quantita_aggiorn = input(
                                    f'La quantità attuale è {oggetti_negozio[nome_prodotto]["quantita"]}, quanto ne vuoi aggiungere?\n').replace(' ','')
                                quantita_agg_check = list(quantita_aggiorn)
                                for num in quantita_agg_check:
                                    if num not in numeri:
                                        check = False
                                if check != False:
                                    quantita_aggiorn = int(quantita_aggiorn)
                                    oggetti_negozio[nome_prodotto]['quantita'] += quantita_aggiorn
                                    oggetti_negozio[nome_prodotto]['totale_fat'] += quantita_aggiorn *oggetti_negozio[nome_prodotto]['prezzo']
                                    oggetti_negozio[nome_prodotto]['totale_fat'] += prezzo_aggiorn * quantita_aggiorn
                                    caricamento_on = False
                                else:
                                    print('Error. Digitare correttamente')
                            else:
                                print('Errore. Digitare correttamente')

            print(oggetti_negozio)
        else:
            totale_fatturato=0
            for item in oggetti_negozio:
                print(f"L'oggetto {oggetti_negozio[item]} è stato venduto {oggetti_negozio[item]['quantita']} volte al prezzo di {oggetti_negozio[item]['prezzo']}, per un fatturato di {oggetti_negozio[item]['totale_fat']} EURO!")
                totale_fatturato +=oggetti_negozio[item]['totale_fat']

            print(f'Il fatturato totale è di {totale_fatturato} Euro')
menu_on = True
numeri= ['0','1','2','3','4','5','6','7','8','9']
oggetti_negozio = {'banana':{
                            'prezzo': 0.75,
                            'quantita': 5,
                            'totale_fat': 3.75}
}

singolo_item={}
while menu_on:
    print('Benvenuto!\nChe operazione vuoi fare?')
    scelta = input('Premi 1 per aggiungere un prodotto da vendere\nPremi 2 per controllo vendite\nPremi 3 per uscire dal programma\n')
    if scelta not in ['1','2','3']:
        print('Si prega di digitare in modo corretto')
    elif scelta=='3':
        menu_on = False
    else:
        if scelta == '1':
            nome_prodotto = input('Iserire il nome prodotto:\n')
            if nome_prodotto not in oggetti_negozio:
                nuovo_prezzo = float(input('Inserisci il prezzo:\n'))
                quantita_venduta= float(input('Quantità venduta:\n'))
                singolo_item['prezzo']=nuovo_prezzo
                singolo_item['quantita']= quantita_venduta
                singolo_item['totale_fat']= quantita_venduta*nuovo_prezzo
                oggetti_negozio[nome_prodotto]={}
                oggetti_negozio[nome_prodotto]=singolo_item
                singolo_item={}
            elif nome_prodotto in oggetti_negozio:
                caricamento_on = True
                while caricamento_on:
                    scelta_caricamento = input('Digita 1 per aggiornare la quantità\nDigita 2 per aggiornare il prezzo\n')
                    if scelta_caricamento not in ['1','2']:
                        print('Si prega di digitare in modo corretto')
                    else:
                        if scelta_caricamento == '1':
                            quantita_aggiorn=float(input(f'La quantità attuale è {oggetti_negozio[nome_prodotto]["quantita"]}, quanto ne vuoi aggiungere?\n'))
                            oggetti_negozio[nome_prodotto]['quantita'] += quantita_aggiorn
                            oggetti_negozio[nome_prodotto]['totale_fat'] += quantita_aggiorn*oggetti_negozio[nome_prodotto]['prezzo']
                            caricamento_on = False
                        if scelta_caricamento == '2':
                            prezzo_aggiorn = float(input(f'Il prezzo attuale è {oggetti_negozio[nome_prodotto]["prezzo"]}, quale è il nuovo prezzo?\n'))
                            oggetti_negozio[nome_prodotto]['prezzo'] = prezzo_aggiorn
                            quantita_aggiorn = float(input(
                                f'La quantità attuale è {oggetti_negozio[nome_prodotto]["quantita"]}, quanto ne vuoi aggiungere?\n'))
                            oggetti_negozio[nome_prodotto]['quantita'] += quantita_aggiorn
                            oggetti_negozio[nome_prodotto]['totale_fat'] += quantita_aggiorn *oggetti_negozio[nome_prodotto]['prezzo']
                            oggetti_negozio[nome_prodotto]['totale_fat'] += prezzo_aggiorn * quantita_aggiorn
                            caricamento_on = False

            print(oggetti_negozio)
        else:
            totale_fatturato=0
            for item in oggetti_negozio:
                print(f"L'oggetto {oggetti_negozio[item]} è stato venduto {oggetti_negozio[item]['quantita']} volte al prezzo di {oggetti_negozio[item]['prezzo']}, per un fatturato di {oggetti_negozio[item]['totale_fat']} EURO!")
                totale_fatturato +=oggetti_negozio[item]['totale_fat']

            print(f'Il fatturato totale è di {totale_fatturato} Euro')
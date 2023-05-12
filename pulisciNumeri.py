numeri= ['0','1','2','3','4','5','6','7','8','9']
split_on = True
a = 0
numeri_unici= []
while split_on:
    numeri_dig = input('Inserisci una secuenza di numeri\n')
    lista_numeri= list(numeri_dig)
    print(lista_numeri)
    #check se ha scritto qualcosa che non va
    for num in lista_numeri:
        if num not in numeri:
            print('Mi dispiace, la secuenza deve essere solo numerica\nRiprova!')
            a = num
            break
        else:
            if int(num) not in numeri_unici:
                numeri_unici.append(int(num))

    if a == 0:
        print(f'I numeri unici sono .\n{numeri_unici}')
        split_on = False
    else:
        split_on = True
        a = 0
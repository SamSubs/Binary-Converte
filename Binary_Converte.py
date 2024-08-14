
while True:
    print(f'{"Menu":^30}\nBinario Para Decimal [1]\nDecimal para Binario [2]\nSair [3]')

    menu = int(input('Opção: '))

    if menu == 1:
        print('Digite um Por Um\nInsira 9 para Parar')
        lista = []
        while True:
            binario = int(input('Digite: '))
            if binario == 9:
                break
            elif binario >= 0 and binario <= 1:
                lista.append(binario)
            elif binario == 9:
                break
        print(lista)
        lista2 = []
        tot = len(lista) - 1
        #print(tot)
        for n in lista:
            print(tot)
            if n == 0:
                tot = tot - 1
                pass
            else:
                cont = pow(2, tot)
                lista2.append(cont)
                tot = tot - 1
                #lista.pop(0)
                #lista.insert(0, t)
                print(n, tot)
        print(lista2)
        soma = 0
        for c in lista2:
            soma = soma + c
        print(soma)
    elif menu == 2:
        pass

    elif menu == 3:
        break

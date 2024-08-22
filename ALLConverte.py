#Ver 2.0
try:
    from Cal_binario import Binario

    while True:
        print(f'{"Menu":^30}\nBinario Para Decimal [1]\nDecimal para Binario [2]\nSair [3]\n')

        menu = int(input('Opção: '))

        if menu == 1:
            print('\n')
            converte = Binario()
            converte.todecimal()
            print('\n')
        elif menu == 2:
            converte_2 = Binario()
            converte_2.tobinary()

        elif menu == 3:
            break
except ValueError as erro:
    print(f'Erro {erro}')

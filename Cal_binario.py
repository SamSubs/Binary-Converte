
class Binario():
    def todecimal(self):
        user = str(input('Digite: ')).strip()

        print('Total Digitado:', len(user), '\nN:', user)

        bits = []

        for c in user:
            if c == '1' or c == '0':
                #print(c)
                bits.append(int(c))
            else:
                pass
        #print(bits)

        #Calculo e contagem
        tot = len(bits) - 1
        lista_bits = []

        for bit in bits:
            if bit == 1:
                calc = 2**tot
                lista_bits.append(calc)
                tot = tot - 1
                print(calc, end=' ')
            else:
                tot = tot - 1
                pass
        print('\nDecimal:', end=' ')
        #print(lista_bits, 'Decimal:', end=' ')

        #Soma
        total = 0
        for s in lista_bits:
            total = total + s
        print(total)

    def tobinary(self):
        user = str(input('Digite: ')).strip()
        user = int(user)

        binary = []
        total = user
        timel = 0.7
        toa = len(str(user))

        if toa >= 3 and toa < 5:
            timel = 0.5
        elif toa >= 5:
            timel = 0.1

        while True:
            import time
            calc = (total/2) % 2
            print('Resto:', str(calc)[2:], end=' ')
            if str(calc)[2:] >= '1' and str(calc)[2:] <= '9':
                binary.append(1)
            else:
                binary.append(0)
            #print('Valor Div:', calc, end=' ')
            time.sleep(timel)

            total = int(total/2)
            print('Atual:', total, end=' ')
            time.sleep(timel)

            print('\n')
            if total/2 >= 0 and total/2 <= 0:
                break
        print('Valor Decimal:', user, '\nBinario²', end=' ') #binary[::-1])
        for t in reversed(binary):
            print(t, end=' ')
        print('\nV ', timel)

#binarytodecimal = Binario()
#binarytodecimal.todecimal()

#decimaltobinary = Binario()
#decimaltobinary.tobinary()

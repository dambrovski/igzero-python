"""
try:
    raise ValueError

except ValueError:
    print('pegamos a exceção')

def teste():
    try:
        a = int(input('escolha um num: '))
        if not 1 <= a <= 20:
                raise ValueError

        else:
                print('obrigado', a)


    except ValueError:
        print('erro')


#teste()
"""

class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    def __str__(self):
        return 'Numero já incluso! %i'%self.num

def main():

    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input('digite um num'))
                break
            except ValueError:
                print('digite apenas numeros')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)

if __name__ == '__main__':
    main()





    










x = open('arquivo.txt', 'w')
x.write('Ola ')
x.write('mundo!')
x.close()

with open('arquivo.txt') as meuArquivo:
        for linha in meuArquivo:
                print(linha)


meuArquivo = open('arquivo.txt')

try:
    for linha in meuArquivo:
            print(linha)

finally:
        meuArquivo.close()


class NossoContextManager:
    def imprime(self, msg):
            print(msg)

    def __enter__(self):
            print('Entrando no bloco with')
            return self

    def __exit__(self, tipo, valor, traceback):
            print(tipo)
            print(valor)
            print(traceback)

with NossoContextManager() as teste:
        teste.imprime('Ola Mundo')
        raise ValueError

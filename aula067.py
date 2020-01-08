"""
try:
    x = int(input('Digite um Numero: '))
    print(x)

except:
    print('erro!')
    x = 0
    
finally:
    print(x)


"""


try:
    a = open('arquivo.txt', 'r')
    linha = a.readline()
    linha.split('!')
    linha = linha[400]
    a.close()
    a = a = open('arquivo.txt', 'a')
    a.write(linha)

except FileNotFoundError:
    print('erro')
    a = open('arquivo.txt', 'w')
    a.write('errooo!!')

finally:
    a.close()

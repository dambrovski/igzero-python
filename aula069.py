"""
try:
    lista = []
    lista.append(int('dsad'))

except IndexError:
        print('Erro!!')

except ValueError:
    print('deu erro de valor')

finally:
        print('Chegamos ao final')

"""
try:
    lista = []
    lista.append(int('aa'))

except (IndexError, ValueError) as excessao:
        print(excessao)
        print('Erro!!')

else:
        print('vamo time!!')

finally:
        print('Chegamos ao final')

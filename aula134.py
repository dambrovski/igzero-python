import csv
f = open('tabela.csv', 'w')

try:
    writer = csv.writer(f)
    writer.writerow( ('Nome', 'Idade', 'Sexo'))
    writer.writerow( ('Lucas', '15', 'M'))
    writer.writerow( ('Luana', '14', 'F'))
    writer.writerow( ('João', '15', 'M'))

finally:
    f.close()

print(open('tabela.csv', 'rt').read())


f = open('tabela.csv', 'r')

try:
    leitor = csv.reader(f)
    for linha in leitor:
        if linha[0] == 'João':
            print('achei')
        print(linha)

finally:
    f.close()

f = open('tabela.csv', 'a')
try:
    writer = csv.writer(f)
    writer.writerow( ('Luke', '15', 'M'))
    writer.writerow( ('Jonas', '14', 'F'))
    writer.writerow( ('Julia', '15', 'M'))

finally:
    f.close()

print(open('tabela.csv', 'rt').read())






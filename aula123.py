def criaClasse(**argumentos):
    return type("MinhaClasse", (object, ), argumentos)

a = criaClasse(idade = 13, olhos = 2)
print(a)
print(a.idade, a.olhos)



class MinhaClasse(object):
    idade = 13
    olhos = 2

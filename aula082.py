"""

l1 = [1,2,3]
l2 = [4,5,6]
#print(zip(l1,l2))
a = zip(l1,l2)
#print(a)
#print(list(a))
l3 = [7,8,9]
l1.append(0)
#print(list(zip(l1,l2,l3)))

lista1 = ['ovos', 'presunto', 'frango', 'carne']
lista2 = [5,2,13]
a = zip(lista1,lista2)
#print(list(zip(lista1,lista2)))
#print(dict(a))

#print(list(lista1[0]))
#print(list(lista1))


for item in lista1:
    print(item)
    
lista1.sort()

i = 0
while True:
    print(lista1[i])
    i = i + 1

"""

#l = [x**2 for x in range(4)]
#print(l)

#lista = [x++2 for x in range(4)]
#print(lista)

l1 = map((lambda x: x**2), range(4))
#print(list(l1))

itensLista = ['ovos', 'presunto', 'frango', 'carne']
lis = map((lambda x: itensLista[x]), range(4))
#print(list(lis))

for item in lis:
    print(item.upper())
    for preco in l1:
        print(preco)
        


#l2 = map((lambda x,y: x + y), range(4), range(3, -1, -1))
#print(list(l2))


def soma(x,y):
    return x + y

"""
l2 = map(soma, range(4), range(3, -1, -1))
print(list(l2))
# 0 + 3, 1 + 2, 2 + , 3 + 0 

#printar apenas os pares
print([x for x in range(5) if x%2 == 0])


def valor(x):
    if x % 2 == 0:
        return x

#vai retornar tudo
print(list(map(valor, range(5))))




a = filter((lambda x: x%2 == 0), range(5))
print(a)
print(list(a))
print(list(a))

"""











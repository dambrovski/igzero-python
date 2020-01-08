#del --> delete --> deletar/apagar
x = 10

del x

#print(x)

l = [1,2,3]
del l[2]
print(l)

#t = (1,2,3)
#del t[2]

s = 'string'
#del s[4]


d = {'1':1, '2':2, '3':3}
del d['1']

print(d)

class Pessoa(object):
    def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade


#joao = Pessoa('Joao', 24)
#del joao.nome
#print(joao.nome)

print([1,2,3] == [1,2,3])
print([1,2,3] is [1,2,3])

l = [1,2,3]
l2 = l
print(l is l2)



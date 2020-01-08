#yeld expressão
"""
def geraQuadrados(n):
    for i in range(n):
        yield i**2


for i in geraQuadrados(5):
    print(i)
        
x = geraQuadrados(5)

print(list(x))
#print(dict(list(enumerate(x))))
print(iter(x) is x)
y = geraQuadrados(5)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

for i in [x**2 for x in range(5)]:
    print(i)

for i in map((lambda x: x**2), range(5)):
    print(i)

def novosQuadrados(n):
    l = []
    for i in range(n):
        l.append(i**2)
    return l

for i in novosQuadrados(5):
    print(i)

"""


def imprime(n):
    for i in range(n):
        x = yield i**2
        print(x)


z = imprime(5)
print(next(z))
print(z.send(5))










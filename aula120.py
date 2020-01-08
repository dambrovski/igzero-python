from collections import defaultdict, deque


def conta_palavras(texto):
    contador = {}
    for palavra in texto.split(' '):
        corrente = contador.get(palavra, 0)
        contador[palavra] = corrente + 1
    return contador


print(conta_palavras('Bom Bom Bom é comer bombom'))


def conta_palavras2(texto):
    contador = defaultdict(int)
    for palavra in texto.split(' '):
        contador[palavra] += 1
    return contador

print(conta_palavras2('Bom Bom Bom é comer bombom'))



d = deque('ghi')

for elem in d: print(elem.upper())

#d.append('j')
d.appendleft('j')
#d.appendright('j')
d.popleft()

print('stop')
for elem in d: print(elem.upper())

d.reverse()
d.remove('i')


print('stop')
for elem in d: print(elem.upper())

print(d.count('g'))


e = deque(d, maxlen = 5)

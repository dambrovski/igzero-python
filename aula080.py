x = open('arquivo.txt')

for i in x:
    print(i)


x.close()

for i in open('arquivo.txt').readlines():
    print(i)

y = open('arquivo.txt').readlines()
print(y)


print(y.__iter__())

z = y.__iter__()
x = open('arquivo.txt')

x = iter(x)

while True:
    try:
        i = next(x)
    except StopIteration:
        break

d = {'1': 1, '2': 2, '3': 3}

print(iter(d.keys()))

#enumerate(['a', 'b', 'c'])
enumerar = enumerate('airton')

for i in enumerar:
    print(i)


















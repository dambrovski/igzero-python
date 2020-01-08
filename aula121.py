import time

class MinhaLista():
    def __getitem__(self, index):
        return index ** 2

a = MinhaLista()

for i in range(5):
    print(a[i])

input()


print("o q acoontec")



t0 = time.time()

"""
for i in a:
    print(i)
    tf = time.time()
    if tf - t0 > 1:
        break
"""

class MinhaLista2(object):
    def __init__(self, tamanho):
        self.len = tamanho

    def __getitem__(self, index):
        if index < self.len:
            return index ** 2
        else:
            raise StopIteration

a = MinhaLista2(5)
            

for i in a:
    print(i)

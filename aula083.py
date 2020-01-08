#all, any, sum e reduce -> functools

print(all([1,0,0,1,1]))
print(all([1,1,1]))
#print(all([1,2,1,2]))

def all(iterable):
    for element in iterable:
        if not element:
                return False
        return True


print(any([1,0,0,1,1]))
print(any([1,1,1]))


def any(iterable):
    for element in iterable:
        if element:
            return False
    return True


l1 = [1,2,3]
print(sum(l1))
print(sum([1,2,3,4.6]))




import functools

def olhe_soma(x,y):
        print ('Adc', x, 'a', y)
        return x + y

print(functools.reduce(olhe_soma, [1,2,3,4,5]))

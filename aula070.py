
"""
try:
    num = 1/0
    int(num)
except Exception as E:
    raise ValueError from E
    print(E)

raise ValueError from SyntaxError


while True:
    try:
        num = int(input('digite um numero entre 1 e 20'))
    except ValueError:
        print('apenas numeros')
    except:
        print('entrada invalida')
    else:
        break

test = True

if not 1<=num<=20:
    test = False

assert test, num


if __debug__:
    if not test:
        raise AssertionError(num)
        
"""

def fazer(x):
    assert x > 0, 'x tem que ser maior que zero'
    return x ** 1/2


print(fazer(-2))













    

import os, time 


"""
def filho():
    print("ola do filho \n", os.getpid())
    os.exit(0)


def pai():
    while True:
        newpid = os.fork()
        if newpid == 0:
            filho()
        else:
            print('ola do pai \n', os.getpid(), newpid)

        if input() == 'q':
            print("closing father", os.getpid())
            break

pai()


def contador(cont):
    for i in range(cont):
        time.sleep(1)
        print('[%s] => %s ' % (os.getpid(), i))


for i in range(5):
    pid = os.fork()
    if pid != 0:
        print("processo %d criado" % pid)
    else:
        contador(5)
        os.exit(0)

print('fim do principal processo')


"""

parm = 0

while True:
    parm += 1
    #copia processo
    pid = os.fork()
    if pid == 0:
        os.execlp('python3', 'python3', 'filho.py', str(parm))
        assert False, 'erro ao iniciar programa'
    else:
        print('filho é: ', pid)
        if input() == 'q': break

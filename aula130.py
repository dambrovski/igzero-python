import _thread as thread, time


"""
def filho(tid):
    print('ola da thread', tid)
    
def pai():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(filho, (i,))
        if input() == 'q': break

pai()
"""

def contador(meuId, cont):
    for i in range(cont):
        time.sleep(1)
        print('[%s] => %s ' % (meuId, i))

for i in range(5):
    thread.start_new_thread(contador, (i, 5))

time.sleep(6)
print("saindoooooooo \n" * 10)

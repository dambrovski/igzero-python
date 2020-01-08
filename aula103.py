import time

#tempo atual e data
print(time.asctime())

#tempo = time.struct_time(tm_year)
#print(tempo)

#localtime
a = time.localtime()
print('ano: ',a[0])
print('mes: ',a[1])
print('dia: ',a[2])


print(time.time())
t0 = time.time()
#time.sleep(2)
tf = time.time()
dt = tf - t0
print(dt)

#espera 10 segundos
#time.sleep(2)


print('contando')
print(time.process_time())

print('oi')

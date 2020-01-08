import dbm
import struct

db = dbm.open('contatos.db', 'c')
#c = create
#r = read
#w = write
#n = abrir novo database

db['Airton'] = 'airton@fkn.com.br'
print(db['Airton'].decode())
#db['Joao'] = str(13)
db['Joao'] = 'joao@fkn.com.br'
print(db['Joao'].decode())
#print(int(db['Joao']))
print(len(db))
print(db.keys())
print('Airton' in db)
#del db['João']

#for key in db:
        #print(key)

#db.pop('Airton')

        
db['jonas'] = struct.pack('I', 13)
print(db['jonas'])
db.close()

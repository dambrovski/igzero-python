import pickle
import shelve

db = shelve.open('shelve.db')


db['usuarios'] = ['root', 'toor']
print(db['usuarios'])
for i in db['usuarios']:
        print(i)

"""
class Pessoa:
    pass

airton = Pessoa()
db['pessoa'] = airton
print(db['pessoa'])

#chave in db

#del db['lista']
db.close()


#db['lista'].append(5)

x = db['lista']
x.append(5)
db['lista'] = x
db.close()

db = shelve.open('shelve.db', writeback = True)

db['lista'].append(6)

"""

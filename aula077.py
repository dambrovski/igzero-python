#java script object notation serializer = json
import json

data = {'Nome': 'Airton', 'RG':123456789, 'CPF': 123456789}
#data = [1,2,3,4]
#data = ('a', 'b', 'c')

data_string = json.dumps(data)
print(data_string)

file = open('test.json', 'wb')
file.write(data_string.encode())

file.close()


file = open('test.json', 'rb')
data_total = file.readline()
print(data_total)
obj1 = json.loads(data_total)
print(obj1)

class Pessoa:
    pass



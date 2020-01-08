import pickle


arq = open('arquivo.pck', 'wb')
l1 = [1,2,3]

pickle.dump(l1, arq)
print(pickle.dumps(l1))


class Pessoa:
      def __init__(self, n, p):
              self.n = n
              self.p = p
      def ola(self):
          print('ola, nome: %s peso %s'%(self.n, self.p))


airton = Pessoa('Airton', 30)
pickle.dump(airton, arq)
arq.close


arq = open('arquivo.pck', 'rb')
x = pickle.load(arq)
print(x)
y = pickle.load(arq)
print('nome',y.n)
print('peso',y.p)
print(y.ola())
arq.close()



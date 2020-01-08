class Conta:
    def __init__ (self, i , s):
            self.ID = i
            self.saldo = s

    def deposito (self, v):
            self.saldo += v
    
    def saque (self, v):
            if self.saldo >= v:
                self.saldo -= v
    def __le__(self, outro):
            if self.ID <= outro.ID:
                
                    return True
            return False
            
    def __eq__(self, outro):
            if self.ID == outro.ID:
                    return True
            return False

    def __ge__(self, outro):
            if self.ID >= outro.ID:
                    return True
            return False

    def __lt__(self, outro):
            if self.ID < outro.ID:
                    return True
            return False
            
    def __gt__(self, outro):
            if self.ID > outro.ID:
                    return True
            return False
            
    def __ne__(self, outro):
            if self.ID != outro.ID:
                    return True
            return False

class Banco:
    def __init__(self):
            self.contas = []

itau = Conta(123,4000)
bradesco = Conta(123,5000)
itau2 = Conta(123,4000)

print(itau==itau2)
print(itau==bradesco)

print(itau.saldo)
itau3 = itau
itau3.deposito(6)
print(itau.saldo)
print(itau3.saldo)

print(id(itau))
print(id(itau3))

#__le__ x <=y
#__eq__ x == y
#__get__ x>=y
#__lt__ x<y
#__gt__ x>y
#__ne__


banco = Banco()
banco.contas = [itau,bradesco]

#print(banco.contas.sort)
print(banco.contas)

class Contas(list):
    def sort(self):
            copia = self.copy()
            tam = len(self)
            self.clear()
            while len(self) < tam:
                    max_id = copia[0]
                    for conta in copia:
                            if conta.ID < min_id:
                                    min_id = conta.ID
                    self.append(min_id)
                    copia.remove(min_id)







            

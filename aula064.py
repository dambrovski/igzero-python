class Conta:
#Objeto do tipo conta, representa uma conta num banco qualquer
    
    def __init__(self, ID, saldo):
        #Construtor da classe conta
            self.ID = ID
            self.saldo = saldo

    def __str__(self):
        #Devolve uma String representando a conta
            return 'ID: %i\nSaldo: R$ %.2f'%(self.ID, self.saldo)

    def __add__ (self,other):
        #Permite somar um conta a outra
            self.saldo += other.saldo

    def __call__ (self,x):
            return x

    #__sub__, __div__, __mult__ obj para obj
            

bradesco = Conta(456, 5000)
itau = Conta(123, 8000)
santander = Conta(789, 600)

print(bradesco)
#bradesco.__add__(10)
itau + bradesco
print(bradesco.saldo)
print(itau.saldo)
#bradesco.__doc__
#bradesco.__str__doc
#funciona somente com comentários usando """ """
#bradesco__help__

class Pai:
    pass

class Filha(Pai):
    pass

class Neta(Filha):
    pass

print(issubclass(Pai,Filha))
print(issubclass(Filha,Pai))
print(issubclass(Neta,Pai))
print(Filha.__bases__)
print(callable(Pai))




















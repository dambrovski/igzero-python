class Vazio:
    def __getattr__(self, atr_nome):
        if atr_nome == 'idade':
            return 40
        else:
            raise AttributeError(atr_nome)


e = Vazio()
print(e.idade)



try:
    e.nome
except AttributeError as E:
    print(E)


class ControleAcesso:
    def __setattr__(self, atr, valor):
        if atr == 'idade':
            self.__dict__[atr] = valor + 10
        else:
            raise AttributeError(atr + ' nao permitido')


c = ControleAcesso()
c.idade = 40
print(c.idade)




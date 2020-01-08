#raise ValueError('spam')
#int('oi')
"""
class NossoContextManager:
        def __enter__(self):
                print('Entramos no bloco with')
        def __exit__(self,tipo,valor,traceback):
                print(tipo)
                print(valor)
                print(traceback)
                
with NossoContextManager() as nosso:
        raise ValueError('spam')

class DeuErro(Exception):
        def __str__(self):
                return 'deu erro justo aogra'

"""
class DeuErroArquivo(Exception):
    def __init__(self, linha, arq):
            self.linha = linha
            self.arq = arq


    def putz(self):
        print('Putz!!')
        

    def __str__(self):
            return 'deu erro na linha \n%s\n do arquivo %s'%(self.linha, self. arq)

  
            
try:
    raise DeuErroArquivo('meu deus', 'arquivo.txt')

except DeuErroArquivo as E:
        print(DeuErroArquivo('meu deus', 'arquivo.txt'))
        print(E)
        E.putz() 

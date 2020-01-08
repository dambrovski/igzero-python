import struct


"""
nome = 'bJoao'
idade = 23
altura = 1.53


code = struct.pack('4s I f', nome.encode(), idade, altura)


arq = open('pessoas.code', 'wb')
arq.write(code)
arq.close

arq = open('pessoas.code', 'rb')
code_ab = arq.readline()


code_desp = struct.unpack('4s I f', code_ab)
print(code_desp)

nome = code_desp[0].decode()
print(nome)

#Ns string de N char, I inteiro pequeno, Q inteiro grande,
#f float pequeno, d float grande,
#? bool



t = (b'Joao', 23, 1.73)

s = struct.Struct('4s I f')

data = s.pack(*t)
print(data)
print(s.unpack(data))


nome = s.unpack(data)[0]
nome.split(b'\n')

"""

import struct

def main():
        pessoas = carregaListaDeCadastros()
        print(pessoas)
        while True:
            cmd = recebeComando()

            if cmd.startswith('n'):
                adicionaCadastro(pessoas)
            elif cmd.startswith('p'):
                if len(pessoas) == 0:
                    print('Não há nenhum cadastro!')
                else:
                    pegaCadastro(pessoas)
            else:
               break
        salvaPessoas(pessoas)


def carregaListaDeCadastros():
    try:
        arq = open('pessoas.decode', 'rb')
    except IOError:
        return{}
    else:
        pessoas = {}
        try:
            for num_char_nome in arq:
                num_char_nome = num_char_nome.split(b'\n')[0]

                decode = '%is Q Q'%struct.unpack('I', num_char_nome)[0]
                data = arq.readline().split(b'\n')[0]
                info = struct.unpack(decode, data)

                pessoas[info[0].decode()] = {'R.G.' : info[1], 'C.P.F.': info[2]}

        except:
            print('há um erro de formatação')
            return{}
        else:
            return pessoas

def recebeComando():
    while True:
        cmd = input('Deseja adc new cadastro ou search?').lower()

        if not cmd.isalpha():
            print('apenas letras')
        elif cmd.startswith('n') or cmd.startswith('p') or cmd.startswith('s'):
            return cmd
        else:
            print('nao entendi o comando')

def adicionaCadastro(pessoas):
    nome = input('digite o nome\n')
    pessoas[nome] = {}
    pegarRG(pessoas[nome])
    pegarCPF(pessoas[nome])


def pegaRG(pessoas):
    while True:
        RG = input('Digite o RG do individuo\n')
        try:
            separado = RG.split('.')
            primeiros_dois = separado[0]
            segundo_tres = separado[1]
            terceiro_tres = separado[2].split('-')[0]
            ultimo = separado[2].split('-')[1]
 
            if not (primeiros_dois.isdigit() and segundo_tres.isdigit() and terceiro_tres.isdigit() and ultimo.isdigit()):
                print('Digite apenas numeros')
 
            elif len(primeiros_dois) != 2 or len(segundo_tres) != 3 or len(terceiro_tres) != 3 or len(ultimo) != 1:
                print('Numero de algarismos está errado, digite novamente')
 
        except IndexError:
            print('Entrada inválida')
 
        except Exception as E:
            print(E)
 
        else:
            pessoas['R.G.'] = int(primeiros_dois+segundo_tres+terceiro_tres+ultimo)
            break
 
def pegaCPF(pessoas):
    while True:
        CPF = input('Digite o CPF do individuo\n')
        try:
            separado = CPF.split('.')
            primeiros_tres = separado[0]
            segundo_tres = separado[1]
            terceiro_tres = separado[2].split('/')[0]
            ultimos_dois = separado[2].split('/')[1]
 
            if not (primeiros_tres.isdigit() and segundo_tres.isdigit() and terceiro_tres.isdigit() and ultimos_dois.isdigit()):
                print('Digite apenas numeros')
 
            elif len(primeiros_tres) != 3 or len(segundo_tres) != 3 or len(terceiro_tres) != 3 or len(ultimos_dois) != 2:
                print('Numero de algarismos está errado, digite novamente')
 
        except IndexError:
            print('Entrada inválida')
 
        except Exception as E:
            print(E)
 
        else:
            pessoas['C.P.F.'] = int(primeiros_tres+segundo_tres+terceiro_tres+ultimos_dois)
            break
 
 
def pegaCadastro(pessoas):
    while True:
        nome = input('Digite o nome da pessoa\n')
 
        if nome in pessoas:
            formataCadastro(pessoas, nome)
            break
        else:
            print('Pessoas nao encontrada, digite novamente')
 
def formataCadastro(pessoas, nome):
    print('Nome: %s'%nome)
    imprimeRG(pessoas[nome]['R.G.'])
    imprimeCPF(pessoas[nome]['C.P.F.'])
    print()
 
def colacaZero(num, palavra):
    if len(palavra) < num:
        return (num - len(palavra))*'0' + palavra
    else:
        return palavra
 
def imprimeRG(RG):
    ultimo = str(RG%10)
    RG //= 10
    terceiro_tres = colacaZero(3, str(RG%1000))
    RG//=1000
    segundo_tres = colacaZero(3, str(RG%1000))
    RG//=1000
    primeiros_dois = colacaZero(2, str(RG%100))
 
    print('R.G.: '+primeiros_dois+'.'+segundo_tres+'.'+terceiro_tres+'-'+ultimo)
 
def imprimeCPF(CPF):
    ultimos_dois = colacaZero(2, str(CPF%100))
    CPF //= 100
    terceiro_tres = colacaZero(3, str(CPF%1000))
    CPF//=1000
    segundo_tres = colacaZero(3, str(CPF%1000))
    CPF//=1000
    primeiros_tres = colacaZero(3, str(CPF%1000))
 
    print('C.P.F: '+primeiros_tres+'.'+segundo_tres+'.'+terceiro_tres+'/'+ultimos_dois)
     
 
def salvaPessoas(pessoas):
    with open('pessoas.decode', 'wb') as arq:
        for nome in pessoas:
            num_de_chars = len(nome)
            num_data = struct.pack('I', num_de_chars)
            arq.write(num_data)
            arq.write(b'\n')
 
            info_data = struct.pack('%is Q Q'%num_de_chars, nome.encode(), pessoas[nome]['R.G.'], pessoas[nome]['C.P.F.'])
 
            arq.write(info_data)
            arq.write(b'\n')
 
if __name__ == '__main__':
    main()
 





















    




























            
                
























            
        









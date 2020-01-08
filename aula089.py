from tkinter import *
import pickle
import shelve

AZUL = '#91B4FF'


"""
def Calcular():
#    resultado['text'] = "Calculando"
    resultado['text'] = form.get()
    resultado['fg'] = "red"

i = Tk()
i.title('Calculadora para Estatisticas')

#tamanho da tela
i.geometry('800x600')

#icone para o app
#i.wm_iconbitmap('icone.ico')

#entrada de texto
form = Entry(i)
form.pack()

#botão calcular
calc = Button(i, text = "Calcule", fg="green", bg="gray", command = Calcular)
calc.pack()

#texto das formulas
resultado = Label(i, text="Resultado", fg="blue")
resultado.pack()


i.mainloop()
"""



class Sistema(object):
    def __init__(self, i):     
        self.db = shelve.open('usuario.db')
        self.db['usuarios'] = ['root','toor']
        logo = PhotoImage(file = 'Imagens/bg_python.gif')
        entrar = PhotoImage(file = 'Imagens/b_entrar.ppm')
        novo = PhotoImage(file = 'Imagens/b_criar.ppm')



        self.logo = Label(i)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        
        #texto do usuario
        self.usuario = Label(i, text="Usuário", fg="blue")
        self.usuario.pack()

    
        

        self.form = Entry(i)
        self.form.pack()


        #texto da senha
        self.senha = Label(i, text="Senha", fg="blue")
        self.senha.pack()

        self.form2= Entry(i)
        self.form2.pack()



   

        self.entrar = Button(i, command = self.verificaLogin)
        self.entrar['image'] = entrar
        self.entrar.image = entrar
        self.entrar.pack(side = LEFT)

        self.novo = Button(i, text = "Entrar", command = self.cadastrarLogin)
        self.novo['image'] = novo
        self.novo.image = novo
        self.novo.pack(side = RIGHT)

        
        #botão entrar
        #self.login = Button(i, text = "Entrar", command = self.verificaLogin)
        #self.login.pack(side = LEFT)

 #       self.novo = Button(i, text = "Novo", command = self.cadastrarLogin)
  #      self.novo.pack(side = RIGHT)

        

        self.logado = Label(i, text=" ")
        self.logado.pack(side = BOTTOM)

        
    def verificaLogin(self):
        
        self.form['text'] = self.form.get()
        self.form2['text'] = self.form2.get()
        usuario = self.form.get()
        senha = self.form2.get()
            
    
        if self.db['usuarios'][0] == usuario:
            mensagem = ""
            validar = True
        else:
            mensagem = "Usuário Inválido"
            if self.db['usuarios'][1] == senha:
                mensagem2 = " %r"%mensagem
                validar = True
            else:
             mensagem2 = "%r senha inválida"%mensagem
             validar = False

        if validar:
            self.logado['text'] = "sucesso"
        else:
           self.logado['text'] = "%r"%mensagem2

    def cadastrarLogin(self):
        self.form['text'] = self.form.get()
        self.form2['text'] = self.form2.get()
        usuario = self.form.get()
        senha = self.form2.get()
    
        if (usuario == "") or (senha == ""):
            self.logado['text'] = "Digite um Usuário e Senha."
        else:
            self.logado['text'] = "Cadastrado com Sucesso!"
            self.db['usuarios'] = [usuario, senha]


i = Tk()
i.title('Login')
Sistema(i)
i['bg'] = AZUL

i.mainloop()

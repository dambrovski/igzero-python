from tkinter import *

"""
#Cria nossa tela


#nome do app
i.title('Ola Mundo')

#tamanho da tela
i.geometry('800x600')

#icone para o app
#i.wm_iconbitmap('icone.ico')

texto = Label(i, text = "Ola Mundo!", bg="red", fg="blue")
texto.pack()

i.mainloop()


i = Tk()
i.title('Brincando')
i.geometry('400x300')
texto = Label(i, text = "Meu texto")
texto.pack()

ent = Entry(i)
ent.pack()

b = Button(i, text="Clique")
b.pack()
#a ordem que os packs forem empacotados, faz diferença

i.mainloop()


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
calc = Button(i, text = "Calcule")
calc.pack()

#texto das formulas
resultado = Label(i, text="Resultado", fg="blue")
resultado.pack()


i.mainloop()

"""

i = Tk()
i.title('Login')

#tamanho da tela
#i.geometry('800x600')

#icone para o app
#i.wm_iconbitmap('icone.ico')

#entrada de texto

#texto do usuario
usuario = Label(i, text="Usuário", fg="blue")
usuario.pack()

form = Entry(i)
form.pack()


#texto da senha
senha = Label(i, text="Senha", fg="blue")
senha.pack()

form2= Entry(i)
form2.pack()



#botão entrar
login = Button(i, text = "Entrar")
login.pack()

i.mainloop()
















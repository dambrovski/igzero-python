from tkinter import *
import pickle
import shelve

AZUL = '#91B4FF'
#xbm, ppm, pgm, gif
#Checkbutton
#partial
#insert
#delete

class Calculadora(object):
    def __init__(self, i):

        self.font = ('Verdana', '20', 'bold')
        self.font2 = ('Verdana', '14', 'bold')

        logo= PhotoImage(file = 'Imagens/bg_python.gif')
        
        #frame que contem os checkbuttons
        self.frame1 = Frame(i)
        self.frame1['bg'] = AZUL

        self.framec = Frame(i)
        self.framec['bg'] = AZUL

        #frame que contem a entrada de texto
        self.frame2 = Frame(i)
        self.frame2['bg'] = AZUL

        #frame que contem o botao de calcular
        self.frame3 = Frame(i)
        self.frame3['bg'] = AZUL

        #frame que contem o texto das formulas
        self.frame4 = Frame(i, pady = 20)
        self.frame4['bg'] = AZUL


        self.framed = Frame(i)
        self.framed['bg'] = AZUL
        
        #frame que contem os botões especificos
        self.frame5 = Frame(i)
        self.frame5['bg'] = AZUL

        #empacotamos as nossas frames
        self.frame1.pack()
        self.framec.pack()
        self.frame2.pack()
        #self.frame2.pack(side = LEFT)
        self.frame3.pack()
        self.framed.pack()
        self.frame4.pack()
        self.frame5.pack()

        #logo do app
        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        #Checkbutton Binomial
        self.bino_s = False
        self.b_binomial = Checkbutton(self.framec, text = 'Modo Binomial', bg = AZUL, font = self.font, command = self.AtvBinomial)
        self.b_binomial.pack(side = LEFT)

        #Checkbutton Poisson
        self.poisson_s  = False
        self.b_poisson = Checkbutton(self.framec, text = 'Modo Poisson', bg = AZUL, font = self.font, command = self.AtvPoisson)
        self.b_poisson.pack(side = LEFT)

        
        #entrada de texto
        self.form = Entry(self.frame2)
        self.form.pack()
    
        #botão calcular
        self.calc = Button(self.frame3, text = "Calcule", bg="#A3FF65", fg="gray", command = self.Calcular, font = self.font)
        self.calc.pack()


        #Entradas váriaveis
        self.l1 = Label(self.framed, text = 'n = ')
        self.e1 = Entry(self.framed)
        self.l2 = Label(self.framed, text = 'p = ')
        self.e2 = Entry(self.framed)
  
        

        #texto as formulas
        self.resultado = Label(self.frame4, text="Resultado", fg="blue", font=self.font2)
        self.resultado.pack()



        botoes = ('Comb(n, k)', 'binomial(n, x, p)',
          'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)',
          'media', 'desvio', 'moda', 'mediana', 'variancia',
          'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)',
          'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)',
          'p(k1 <= x <= k2)')



        for i in range(len((botoes))):
            if i % 3 == 0:
                subframe = Frame(self.frame5)
                subframe.pack()    
            a = Button(subframe, text = botoes[i], bg = 'green', width=25, command = (lambda : self.ColocaTexto(botoes[i])))
            a.pack(side = LEFT)

        self.delete = Button(subframe, text='del', bg='red', width=25, command = self.Del)
        self.delete.pack(side = LEFT)


    def MostraElementos(self):
        self.l1.pack(side = LEFT)
        self.e1.pack(side = LEFT)
        self.l2.pack(side = LEFT)
        self.e2.pack(side = LEFT)



    def SomeElementos(self):
        self.l1.pack_forget()
        self.e1.pack_forget()
        self.l2.pack_forget()
        self.e2.pack_forget()
        
        
    def Del(self):
        self.form.delete(0, END)

    def ColocaTexto(self, texto):
        self.form.insert(END, texto)
        

    def MSG(self, text, cor = 'red'):
        self.resultado['text'] = text
        self.resultado['fg'] = cor

    def Calcular(self):
        self.form.delete(0, END)
        self.MSG(self.form.get(), 'green')
    #   resultado['text'] = "Calculando"


    def ConfBino(self):
        self.l1['text'] = 'n = '
        self.l2['text'] = 'p = '

    def ConfPoisson(self):
        self.l1['text'] = 'l = '
        self.l2['text'] = 't = '

    
    
    
    def AtvBinomial(self):
        self.bino_s = not self.bino_s
        if self.bino_s:
            self.MSG('Bino ativo')
            self.MostraElementos()
            if self.poisson_s:
                self.poisson_s = False
                self.b_poisson.deselect()
            else:
                self.MostraElementos()
            self.ConfBino()
        else:
            self.MSG('Bino desativado', cor = 'black')
            self.SomeElementos()

        
    def AtvPoisson(self):   
        self.poisson_s = not self.poisson_s
        if self.poisson_s:
            self.MSG('Poisson ativo')
            self.MostraElementos()
            if self.bino_s:
                self.bino_s = False
                self.b_binomial.deselect()
            else:
                self.MostraElementos()
            self.ConfPoisson()                
        else:
            self.MSG('Poisson desativado', cor = 'black')
            self.SomeElementos()
        


i = Tk()

#criamos uma instancia da calculadora
Calculadora(i)

i.title('Calculadora para Estatisticas')

#tamanho da tela
i.geometry('800x600')

#definir cor de background
i['bg'] = AZUL

#icone para o app
#i.wm_iconbitmap('icone.ico')


    
i.mainloop()

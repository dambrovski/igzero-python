from tkinter import *
import pickle
import shelve

AZUL = '#91B4FF'
#xbm, ppm, pgm, gif


class Calculadora(object):
    def __init__(self, i):

        self.font = ('Verdana', '20', 'bold')
        self.font2 = ('Verdana', '14', 'bold')

        logo= PhotoImage(file = 'Imagens/bg_python.gif')
        
        #frame que contem os checkbuttons
        self.frame1 = Frame(i)
        self.frame1['bg'] = AZUL

        #frame que contem a entrada de texto
        self.frame2 = Frame(i)
        self.frame2['bg'] = AZUL

        #frame que contem o botao de calcular
        self.frame3 = Frame(i)
        self.frame3['bg'] = AZUL

        #frame que contem o texto das formulas
        self.frame4 = Frame(i, pady = 20)
        self.frame4['bg'] = AZUL

        #frame que contem os botões especificos
        self.frame5 = Frame(i)
        self.frame5['bg'] = AZUL

        #empacotamos as nossas frames
        self.frame1.pack()
        self.frame2.pack()
        #self.frame2.pack(side = LEFT)
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #logo do app
        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()
        
        #entrada de texto
        self.form = Entry(self.frame2)
        self.form.pack()
    
        #botão calcular
        self.calc = Button(self.frame3, text = "Calcule", bg="#A3FF65", fg="gray", command = self.Calcular, font = self.font)
        self.calc.pack()

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
            a = Button(subframe, text = botoes[i], bg = 'green', width=25)
            a.pack(side = LEFT)

        self.delete = Button(subframe, text='del', bg='red', width=25)
        self.delete.pack(side = LEFT)



    def Calcular(self):
    #   resultado['text'] = "Calculando"
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = "green"
  



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

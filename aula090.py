from tkinter import *
import pickle
import shelve


class Calculadora(object):
    def __init__(self, toplevel):
    
        #entrada de texto
        self.form = Entry(i)
        self.form.pack()
    
        #botão calcular
        self.calc = Button(i, text = "Calcule", fg="green", bg="gray", command = self.Calcular)
        self.calc.pack()

        #texto as formulas
        self.resultado = Label(i, text="Resultado", fg="blue")
        self.resultado.pack()


        botoes = ('Comb(n, k)', 'binomial(n, x, p)',
          'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)',
          'media', 'desvio', 'moda', 'mediana', 'variancia',
          'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)',
          'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)',
          'p(k1 <= x <= k2)')

        for x in (botoes):
                a = Button(i, text = x, bg = 'green')
                a.pack()

    def Calcular(self):
    #   resultado['text'] = "Calculando"
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = "red"
  



i = Tk()

#criamos uma instancia da calculadora
Calculadora(i)

i.title('Calculadora para Estatisticas')

#tamanho da tela
i.geometry('800x600')

#icone para o app
#i.wm_iconbitmap('icone.ico')


    
i.mainloop()

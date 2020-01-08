from tkinter import *
from constantes import *
 
from retangulo import Retangulo
from bola import Bola
import random

#Canvas: itemconfig, id, delete, tag, move
#Tk: after
class Jogo(object):
    """
    Classe que organiza os elementos do jogo
    """
    def __init__(self):
        #Criamos o conteiner principal do jogo
        self.root = Tk()
        self.root.geometry('%ix%i'%(LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Pong')
 
        #E uma frame para conter o canvas
        self.frame=Frame(bg="black")
        self.frame.pack()
         
        #Criamos a tela do jogo
        self.canvas = Canvas(self.frame, bg="black",width=CANVAS_L,height=CANVAS_A, cursor = 'target')
        self.canvas.pack()
 
        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START', command = self.começa)
        self.começar.focus_force()
        self.começar.pack()

        #bind com a tecla enter
        
        self.começar.bind('<Return>', self.começa)
        
        
 
        #self.canvas.create_polygon((100, 200), (150, 250), (250, 250), (300, 200), (300, 100), (250, 50), (150, 50), (100, 100), fill = 'white')
 
        self.novoJogo()
 
        self.root.mainloop()
 
    def novoJogo(self):
        """
        Cria os elementos de um novo jogo

        """
        #criar a bola q irá se movimentar
        self.bola = Bola(raio = 30, cor='red', pos = (100,200), vel = (3,3))

        #criar player tbm
        self.player = Retangulo(largura = 100, altura = 20, cor = 'green', pos = (LARGURA//2 + 100, 350), vel = (15,15), tag='player')
        #self.player = self.canvas.create_rectangle((CANVAS_L//2, 350), (CANVAS_L//2 + 100, 370), fill = 'green', tag='player')
        self.player.desenhar(self.canvas)


        #adicionar o evento de movimentação com o uso do teclado
        self.canvas.bind('<Motion>', self.move_player)
        #criar arco dentro da bola
        #self.canvas.create_arc(p[0], p[1], p[0] + raio, p[1] + raio, fill='orange', start=60, extent = 90, tag='bola')

        #Lista dos retângulos
        self.r = []
 
         
 
        #E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2 #linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 50 #Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['green', 'orange', 'white', 'lightgray', 'yellow', 'purple'])
            for j in range(c):
                r = self.canvas.create_rectangle(b*j+(j+1)*e, i*h+(i+1)*e + y0,b*j+(j+1)*e + b, i*h+(i+1)*e + y0 + h, fill = cor, tag='rect')
                self.r.append(r)
        #self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text = 'OLA COLEGA!', fill = 'white')
        
        #cria bola do jogo
     
        self.jogando = True

    def começa(self, event):
        """
        inicia jogo
        """
        self.jogar()


    def jogar(self):
        
        """jogo rodando"""
        if self.jogando:
            self.update()
            self.desenhar()
            
            self.root.after(10, self.jogar)
        else:
            self.acabou(self.msg)


    def move_player(self, event):
        """
        move o player na tela de acordo com o movimento do mouse
        """
        if event.x > 0 and event.x < CANVAS_L - self.player.b:
            self.player.x = event.x


    def update(self):
        
        """update condições de jogo"""
        self.bola.update(self)
       
        #caçar por colisoes
        #self.VerificaColisao()


    def desenhar(self):
        """metodo para redesenhar a tela do jogo"""
        #self.canvas.delete(self.bola)
        #self.canvas.delete('bola')
        #self.canvas.delete('arc')
        #self.bola = self.canvas.create_oval(self.b_x, self.b_y, self.b_x + 30, self.b_y + 30, fill='red', outline='white', tag='bola') 
        #self.canvas.create_arc(self.b_x, self.b_y, self.b_x + 30, self.b_y + 30,fill='orange', start=60, extent = 90, tag='bola')    
        pass
    
    
    def VerificaColisao(self):
       #verifica se houve alguma colisão entre elementos do jogo
        #primeiro criamos uma bounding box para a bola
        coord = self.canvas.bbox('bola')
        #x1, y1, x2, y2

        #depois pegamos a id de todos os objetos que colidem com a bola
        colisoes = self.canvas.find_overlapping(*coord)

        #se o numero de colisoes for diferente de zero
        if len(colisoes) != 0:
            #Verificamos se a id do objeto é diferente do player
            if colisoes[0] != self.player:
                #vamos checar se ha colisão cm o objeto mais proximo do
                #topo esquerdo da bola
                m_p = self.canvas.find_closest(coord[0], coord[1])

                #depois temos que olhar para cada um dos retangulos para
                #identificar com q bola colidiu

                for r in self.r:
                    #tendo encontrado o retangulo
                    if r == m_p[0]:
                        #deletamos ele do jogo
                        self.r.remove(r)
                        self.canvas.delete(r)

                        #e invertemos o sentido da velocidade da bola
                        self.b_vy *= -1

                        #por fim sai fora
                        return
                


 
if __name__ == '__main__':
    Jogo()

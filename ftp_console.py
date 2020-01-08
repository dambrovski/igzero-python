1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
"""
#################################################################################
Utiliza a função criada getfile com uma classe que de formulário reutilizável.
#################################################################################
"""
 
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import ftp_download_org, ftp_upload, os, sys, _thread
 
class FtpForm(object):
    def __init__(self):
        # Primeiro nós criamos uma instância de tk
        self.root = Tk()
 
        # Damos um título ao aplicativo
        self.root.title("FTP GUI")
 
        # Criamos as labels indicando os campos a serem preenchidos
        labels = ['Nome do Servidor', 'Diretório Remoto', 'Nome do Arquivo', 'Diretório Local', 'Usuário?', 'Senha?']
 
        # Dicionário que contem todas as entrys com as respectivas labels
        # utilizadas
        self.content = {}
 
        # Cria labels e caixas de entrada de texto utilizadas
        self.frame1 = Frame(self.root)
        self.cria_labels(labels, self.frame1)
        self.frame1.pack()
 
        # Criamos a segunda frame que contem os radio buttons
        self.frame2 = Frame(self.root)
        self.d = Radiobutton(self.frame2, text="Download", value=1, command=self.select1)
        self.d.grid(row=1, column=1)
        self.u = Radiobutton(self.frame2, text="Upload", value=2, command=self.select2)
        self.u.grid(row=1, column=2)
        self.flag = 2
        self.frame2.pack()
 
        # Criamos a terceira frame para conter o botão de submissão
        self.submit = Button(self.root, text="Submit", command=self.submit)
        self.submit.pack()
  
        # Vamos utilizar threads para fazer com que a janela do aplicativo
        # não trave quando um download estiver sendo realizado
        self.mutex = _thread.allocate_lock()
        self.threads = 0
 
        # Associa o fechamento a função de cancelamento
        self.root.protocol("WM_DELETE_WINDOW", self.cancel)
 
    def cria_labels(self, labels, frame):
        """
        Cria todas as labels e entradas de texto utilizadas
        ;paramn labels: list de strs contendo o nome das labels
        ;paramn frame: tkinter.Frame contendo os widgets
        """
        for i in range(len(labels)):
            Label(frame, text=labels[i]).grid(row=i, column=1)
            self.content[labels[i]] = Entry(frame)
            self.content[labels[i]].grid(row=i, column=2)
 
    def select1(self):
        self.flag = 1
 
    def select2(self):
        self.flag = 2
 
    def submit(self):
        """
        Envia o comando de operação
        """
        # Obtem os dados informados nas entradas
        localdir = self.content['Diretório Local'].get()
        remotedir = self.content['Diretório Remoto'].get()
        servername = self.content['Nome do Servidor'].get()
        filename = self.content['Nome do Arquivo'].get()
        username = self.content['Usuário?'].get()
        password = self.content['Senha?'].get()
        userinfo = ()
 
        # Obtém o login e senha caso ambos sejam nao nulos
        if username and password:
            userinfo = (username, password)
        if localdir:
            os.chdir(localdir)
 
        # Obtem um espaço para executar uma nova thread
        self.mutex.acquire()
        self.threads += 1
        self.mutex.release()
 
        # Inicializa a nova thread
        if self.flag == 1:
            ftpargs = (filename, servername, remotedir, userinfo)
            _thread.start_new_thread(self.download, ftpargs)
        else:
            ftpargs = (os.path.join(localdir, filename), servername, remotedir, userinfo)
            _thread.start_new_thread(self.upload, ftpargs)
 
    def download(self, filename, servername, remotedir, userinfo):
        """
        Transfere o arquivo indicado para o servidor
        ;paramn filename: str caminho para o arquivo a ser transferido
        ;paramn servername: str domínimo do servidor
        ;paramn remotedir: str diretório remoto
        """
        try:
            ftp_download_org.getfile(filename, servername, remotedir, userinfo, verbose=False, refetch=True)
            showinfo("Download", "Download do arquivo %s foi concluído"%filename)
        except:
            showerror("Download", "Download do arquivo " + filename + "falhou\n" + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]))
 
        self.mutex.acquire()
        self.threads -= 1
        self.mutex.release()
 
    def upload(self, filename, servername, remotedir, userinfo):
        """
        Transfere o arquivo indicado para o servidor
        ;paramn filename: str caminho para o arquivo a ser transferido
        ;paramn servername: str domínimo do servidor
        ;paramn remotedir: str diretório remoto
        """
        try:
            ftp_upload.manda_arquivo(filename, servername, remotedir, userinfo, verbose=False)
            showinfo("Upload", "Upload do arquivo %s foi concluído"%filename)
        except:
            showerror("Upload", "Upload do arquivo " + filename + "falhou\n" + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]))
 
        self.mutex.acquire()
        self.threads -= 1
        self.mutex.release()
 
 
    def cancel(self):
        if self.threads == 0:
            Tk().quit()
        else:
            showinfo("FTP GUI", 'Não pode sair: %d threads executando' % self.threads)
 
if __name__ == '__main__':
    f = FtpForm()
    f.root.mainloop()


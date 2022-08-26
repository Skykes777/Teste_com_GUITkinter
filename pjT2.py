from tkinter import *

class Tela:
    def __init__(self) -> None:
        self.root = Tk()
        self.itens_tela()
        self.frames_tela()
        self.botoes_f1()
        self.entradas_dados()
        self.root.mainloop()

    def itens_tela(self) -> None:
        self.root.title('Teste de GUI com Tkinter')
        self.root.configure(background='#ADD8E6')
        self.root.resizable(True, True)
        self.root.geometry('1000x800')
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=1000, height=800)

    def frames_tela(self) -> None:
        # frame de címa
        self.f1 = Frame(self.root, bg='#F0F8FF', highlightbackground='#B0C4DE', highlightthickness=4)
        self.f1.place(relx=0.02, rely=0.04, relwidth=0.95, relheight=0.45)
        # frame de baixo
        self.f2 = Frame(self.root, bg='#F0F8FF', highlightbackground='#B0C4DE', highlightthickness=4)
        self.f2.place(relx=0.02, rely=0.5, relwidth=0.95, relheight=0.45)

    def botoes_f1(self) -> None:
        # botão de limpar
        self.bt1 = Button(self.f1, text='Limpar', bg='#87CEEB')
        self.bt1.place(relx=0.19, rely=0.1, relwidth=0.1, relheight=0.1)
        # botão de buscar
        self.bt2 = Button(self.f1, text='Buscar', bg='#87CEEB')
        self.bt2.place(relx=0.29, rely=0.1, relwidth=0.1, relheight=0.1)
        # botão de novo
        self.bt3 = Button(self.f1, text='Novo', bg='#87CEEB')
        self.bt3.place(relx=0.60, rely=0.1, relwidth=0.1, relheight=0.1)
        # botão de alterar
        self.bt4 = Button(self.f1, text='Alterar', bg='#87CEEB')
        self.bt4.place(relx=0.70, rely=0.1, relwidth=0.1, relheight=0.1)
        # botão de apagar
        self.bt5 = Button(self.f1, text='Apagar', bg='#87CEEB')
        self.bt5.place(relx=0.80, rely=0.1, relwidth=0.1, relheight=0.1)

    def entradas_dados(self) -> None:
        # label do código
        self.label_codigo = Label(self.f1, text='Código', bg='#F0F8FF')
        self.label_codigo.place(relx=0.07, rely=0.08)
        # entrada de dados do código
        self.entrada_dados = Entry(self.f1)
        self.entrada_dados.place(relx=0.07, rely=0.14, relwidth=0.1)

        # label nome
        self.label_nome = Label(self.f1, text='Nome', bg='#F0F8FF')
        self.label_nome.place(relx=0.07, rely=0.3)
        # entrada de dados no nome
        self.entrada_nome = Entry(self.f1)
        self.entrada_nome.place(relx=0.07, rely=0.4, relheight=0.1, relwidth=0.83)

        # label do telefone
        self.label_telefone = Label(self.f1, text='Telefone', bg='#F0F8FF')
        self.label_telefone.place(relx=0.07, rely=0.6)
        # entrada de dados do telefone
        self.entrada_telefone = Entry(self.f1)
        self.entrada_telefone.place(relx=0.07, rely=0.7, relwidth=0.40, relheight=0.1)

        # labem da cidade
        self.label_cidade = Label(self.f1, text='Cidade', bg='#F0F8FF')
        self.label_cidade.place(relx=0.50, rely=0.6)
        # entrada de dados da cidade
        self.entrada_cidade = Entry(self.f1)
        self.entrada_cidade.place(relx=0.50, rely=0.7, relwidth=0.40, relheight=0.1)

Tela()

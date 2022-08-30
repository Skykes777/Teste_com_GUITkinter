from tkinter import *
from tkinter import ttk

class Tela():
    def __init__(self) -> None:
        self.janela = Tk()
        self.configurações_basicas()
        self.frames_janela()
        self.labels_entradas_botoes()
        self.lista_frame2()
        self.janela.mainloop()

    def configurações_basicas(self) -> None:
        self.janela.title('Teste de software com Tkinter')
        self.janela.configure(background='#4682B4')
        self.janela.resizable(True, True)
        self.janela.geometry('1000x800')
        self.janela.maxsize(width=1920, height=1080)
        self.janela.minsize(width=1000, height=800)

    def frames_janela(self) -> None:
        self.f1 = Frame(self.janela, bg='#F0FFFF')
        self.f1.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)

        self.f2 = Frame(self.janela, bg='white')
        self.f2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)

    def labels_entradas_botoes(self) -> None:
        # botão limpar
        botao_limpar = Button(self.f1, text='Limpar', bd=2,
                              bg='#1E90FF', fg='white', font=('arial', 14, 'bold'))
        botao_limpar.place(relx=0.25, rely=0.14, relwidth=0.1, relheight=0.1)
        # botão buscar
        botao_buscar = Button(self.f1, text='Buscar', bd=2,
                              bg='#1E90FF', fg='white', font=('arial', 14, 'bold'))
        botao_buscar.place(relx=0.35, rely=0.14, relwidth=0.1, relheight=0.1)
        # botão novo
        botao_novo = Button(self.f1, text='Novo', bd=2,
                            bg='#1E90FF', fg='white', font=('arial', 14, 'bold'))
        botao_novo.place(relx=0.60, rely=0.14, relwidth=0.1, relheight=0.1)
        # botão alterar
        botao_alterar = Button(self.f1, text='Alterar', bd=2,
                               bg='#1E90FF', fg='white', font=('arial', 14, 'bold'))
        botao_alterar.place(relx=0.70, rely=0.14, relwidth=0.1, relheight=0.1)
        # botão apagar
        botao_limpar = Button(self.f1, text='Apagar', bd=2,
                              bg='#1E90FF', fg='white', font=('arial', 14, 'bold'))
        botao_limpar.place(relx=0.80, rely=0.14, relwidth=0.1, relheight=0.1)

        ############################################################################################################

        # label  e entrada do código
        self.label_codigo = Label(
            self.f1, text='Código', bg='#F0FFFF', fg='#1E90FF', font=('arial', 13, 'bold'))
        self.label_codigo.place(relx=0.10, rely=0.06)
        self.entrada_codigo = Entry(self.f1)
        self.entrada_codigo.place(
            relx=0.10, rely=0.14, relheight=0.1, relwidth=0.1)
        # label e entrada do nome
        self.label_codigo = Label(
            self.f1, text='Nome', bg='#F0FFFF', fg='#1E90FF', font=('arial', 13, 'bold'))
        self.label_codigo.place(relx=0.10, rely=0.3)
        self.entrada_codigo = Entry(self.f1)
        self.entrada_codigo.place(
            relx=0.10, rely=0.4, relheight=0.1, relwidth=0.80)
        # labem e entrada do telefone
        self.label_codigo = Label(
            self.f1, text='Telefone', bg='#F0FFFF', fg='#1E90FF', font=('arial', 13, 'bold'))
        self.label_codigo.place(relx=0.10, rely=0.6)
        self.entrada_codigo = Entry(self.f1)
        self.entrada_codigo.place(
            relx=0.10, rely=0.7, relheight=0.1, relwidth=0.38)
        # label e entrada da cidade
        self.label_codigo = Label(
            self.f1, text='Cidade', bg='#F0FFFF', fg='#1E90FF', font=('arial', 13, 'bold'))
        self.label_codigo.place(relx=0.52, rely=0.6)
        self.entrada_codigo = Entry(self.f1)
        self.entrada_codigo.place(
            relx=0.52, rely=0.7, relheight=0.1, relwidth=0.38)

    def lista_frame2(self) -> None:
        self.listaCLI = ttk.Treeview(self.f2, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaCLI.heading('#0', text='')
        self.listaCLI.heading('#1', text='Código')
        self.listaCLI.heading('#2', text='Nome')
        self.listaCLI.heading('#3', text='Telefone')
        self.listaCLI.heading('#4', text='Cidade')

        self.listaCLI.column('#0', width=1)
        self.listaCLI.column('#1', width=50)
        self.listaCLI.column('#2', width=200)
        self.listaCLI.column('#3', width=125)
        self.listaCLI.column('#4', width=125)

        self.listaCLI.place(relx=0.0, rely=0.0, relwidth=0.98, relheight=0.99)

        self.scroolBar = Scrollbar(self.f2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroolBar.set)
        self.scroolBar.place(relx=0.98, relwidth=0.02, relheight=0.99)

Tela()

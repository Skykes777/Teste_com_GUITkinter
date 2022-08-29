import re
from tkinter import *
from tkinter import ttk

class Aplication():
    def __init__(self) -> None:
        self.janela = Tk()
        self.Tela()
        self.Frames_de_tela()
        self.botoes()
        self.lista_frame2()
        self.janela.mainloop()

    def Tela(self) -> None:
        self.janela.title('Teste de Janela Tkinter')
        self.janela.configure(background='#6495ED')
        self.janela.geometry('1000x800')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=1920, height=1080)
        self.janela.minsize(width=1000, height=800)

    def Frames_de_tela(self) -> None:
        self.frame_1 = Frame(self.janela, bg='#F0F8FF', highlightbackground='#B0E0E6', highlightthickness=4)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.janela, bg='#F0F8FF', highlightbackground='#B0E0E6', highlightthickness=4)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def botoes(self) -> None:
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.15, relwidth=0.1, relheight=0.10)

        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.15, relwidth=0.1, relheight=0.10)

        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.15, relwidth=0.1, relheight=0.10)

        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.15, relwidth=0.1, relheight=0.10)

        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.15, relwidth=0.1, relheight=0.10)

        ###########################---Label código---#######################################
        self.lb_codigo = Label(self.frame_1, text='Código', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_codigo.place(relx=0.05, rely=0.09)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.16, relwidth=0.09, relheight=0.09)

        ###########################---Label Nome---##########################################

        self.lb_nome = Label(self.frame_1, text='Nome', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85, relheight=0.09)

        ###########################---Label Telefone#########################################

        self.lb_telefone = Label(self.frame_1, text='Telefone', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.nome_telefone = Entry(self.frame_1)
        self.nome_telefone.place(relx=0.05, rely=0.7, relwidth=0.40, relheight=0.09)

        ###########################---Label Cidade---########################################

        self.lb_cidade = Label(self.frame_1, text='Cidade', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.nome_cidade = Entry(self.frame_1)
        self.nome_cidade.place(relx=0.5, rely=0.7, relwidth=0.40, relheight=0.09)

    def lista_frame2(self) -> None:
        self.listaClI = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaClI.heading('#0', text='')
        self.listaClI.heading('#1', text='Código')
        self.listaClI.heading('#2', text='Nome')
        self.listaClI.heading('#3', text='Telefone')
        self.listaClI.heading('#4', text='Cidade')

        self.listaClI.column('#0', width=1)
        self.listaClI.column('#1', width=50)
        self.listaClI.column('#2', width=200)
        self.listaClI.column('#3', width=125)
        self.listaClI.column('#4', width=125)

        self.listaClI.place(relx=0.0, rely=0.0, relwidth=0.98, relheight=0.99)

        self.scroollinha = Scrollbar(self.frame_2, orient='vertical')
        self.listaClI.configure(yscroll=self.scroollinha.set)
        self.scroollinha.place(relx=0.98, relwidth=0.02, relheight=0.99)


Aplication()

from tkinter import *
from tkinter import ttk
import sqlite3

class Func:
    def limpar_tela(self) -> None:
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conectar_bd(self) -> None:
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    
    def desconectar_bd(self) -> None:
        self.conn.close(); print('Desconectando banco de dados')
    
    def montar_tabelas(self) -> None:
        self.conectar_bd()
        # criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente TEXT(40) NOT NULL,
                telefone INTEGER(20),
                cidade TEXT(40)
            );
        """)
        self.conn.commit(); print('Banco de dados criado') 
        self.desconectar_bd()

    def add_cliente(self) -> None:
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conectar_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))

        self.conn.commit()
        self.select_lista()
        self.desconectar_bd()
        self.limpar_tela()

    def select_lista(self) -> None:
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conectar_bd()
        
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCLI.insert('', END, values=i)
        self.desconectar_bd()

###################################################################################################

class Aplication(Func):
    def __init__(self) -> None:
        self.janela = Tk()
        self.Tela()
        self.Frames_de_tela()
        self.botoes()
        self.lista_frame2()
        self.montar_tabelas()
        self.select_lista()
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
        # botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.2, rely=0.15, relwidth=0.1, relheight=0.10)
        # botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.15, relwidth=0.1, relheight=0.10)
        # botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.15, relwidth=0.1, relheight=0.10)
        # botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#4169E1', fg='white', font=('arial', 11, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.15, relwidth=0.1, relheight=0.10)
        # botão apagar
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

        self.lb_fone = Label(self.frame_1, text='Telefone', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_fone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.40, relheight=0.09)

        ###########################---Label Cidade---########################################

        self.lb_cidade = Label(self.frame_1, text='Cidade', font=('verdan', 11, 'bold'), bg='#F0F8FF', fg='#4169E1')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.40, relheight=0.09)

    def lista_frame2(self) -> None:
        self.listaCLI = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
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

        self.scroollinha = Scrollbar(self.frame_2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroollinha.set)
        self.scroollinha.place(relx=0.98, relwidth=0.02, relheight=0.99)

    
Aplication()

from tkinter import *
from tkinter import ttk
import sqlite3

class Funcs:
    def limpar_tela(self) -> None:
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_fone.delete(0, END)
        self.entry_cidade.delete(0, END)

    def conectar_db(self) -> None:
        self.banco1 = sqlite3.connect('bancoD.db')
        self.cusor1 = self.banco1.cursor(); print('Conectando ao banco de dados')

    def desconectar_db(self) -> None:
        self.banco1.close(); print('Desconectando banco de dados')

    def montar_db(self) -> None:
        self.conectar_db()
        self.cusor1.execute("""
            CREATE TABLE IF NOT EXISTS bancoD (
                cod INTEGER PRIMARY KEY,
                nome_cliente TEXT(40) NOT NULL,
                email TEXT(40) NOT NULL,
                telefone INTEGER(20) NOT NULL,
                cidade TEXT(40) NOT NULL
            );
        """)
        self.banco1.commit(); print('Criando banco de dados')
        self.desconectar_db()
    
    def add_cliente(self) -> None:
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.email = self.entry_email.get()
        self.fone = self.entry_fone.get()
        self.cidade = self.entry_cidade.get()
        self.conectar_db()

        self.cusor1.execute(""" INSERT INTO bancoD (nome_cliente, email, telefone, cidade)
        VALUES (?, ?, ?, ?)""", (self.nome, self.email, self.fone, self.cidade))
        self.banco1.commit()
        self.desconectar_db()
        self.select_lista()
        self.limpar_tela()
    
    def select_lista(self) -> None:
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conectar_db()

        lista = self.cusor1.execute(""" SELECT cod, nome_cliente, email, telefone, cidade FROM bancoD
        ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCLI.insert('', END, values=i)
        self.desconectar_db()

class TelaGUI(Funcs):
    def __init__(self) -> None:
        self.janela = Tk()
        self.configurações_basicas()
        self.frames_tela()
        self.botoes_labels_entradas()
        self.lista_frame2()
        self.montar_db()
        self.select_lista()
        self.janela.mainloop()
    
    def configurações_basicas(self) -> None:
        self.janela.title('Teste de software Tkinter')
        self.janela.configure(background='#778899')
        self.janela.resizable(True, True)
        self.janela.geometry('1000x800')
        self.janela.minsize(width=1000, height=800)
        self.janela.maxsize(width=1920, height=1080)
    
    def frames_tela(self) -> None:
        self.f1 = Frame(self.janela, bg='#F0F8FF')
        self.f1.place(relx=0.02, rely=0.03, relheight=0.45, relwidth=0.96)

        self.f2 = Frame(self.janela, bg='white')
        self.f2.place(relx=0.02, rely=0.51, relheight=0.45, relwidth=0.96)
    
    def botoes_labels_entradas(self) -> None:
        # botão limpar
        self.bt_limpar = Button(self.f1, text='Limpar', bd=2, fg='white', bg='#4682B4', font=('arial', 14, 'bold'), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.26, rely=0.19, relwidth=0.1, relheight=0.1)
        # botão buscar
        self.bt_buscar = Button(self.f1, text='Buscar', bd=2, fg='white', bg='#4682B4', font=('arial', 14, 'bold'))
        self.bt_buscar.place(relx=0.36, rely=0.19, relwidth=0.1, relheight=0.1)
        # botão novo
        self.bt_novo = Button(self.f1, text='Novo', bd=2, fg='white', bg='#4682B4', font=('arial', 14, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.59, rely=0.19, relwidth=0.1, relheight=0.1)
        # botão alterar
        self.bt_alterar = Button(self.f1, text='Alterar', bd=2, fg='white', bg='#4682B4', font=('arial', 14, 'bold'))
        self.bt_alterar.place(relx=0.69, rely=0.19, relwidth=0.1, relheight=0.1)
        # botão Apagar
        self.bt_limpar = Button(self.f1, text='Apagar', bd=2, fg='white', bg='#4682B4', font=('arial', 14, 'bold'))
        self.bt_limpar.place(relx=0.79, rely=0.19, relwidth=0.1, relheight=0.1)

        ##############################################################################################################

        # label e entry código
        self.label_codigo = Label(self.f1, text='Código', fg='#4682B4', bg='#F0F8FF', font=('arial', 14, 'bold'))
        self.label_codigo.place(relx=0.11, rely=0.11)
        self.entry_codigo = Entry(self.f1)
        self.entry_codigo.place(relx=0.11, rely=0.19, relwidth=0.1, relheight=0.1)
        # label e entry nome
        self.label_nome = Label(self.f1, text='Nome', fg='#4682B4', bg='#F0F8FF', font=('arial', 14, 'bold'))
        self.label_nome.place(relx=0.11, rely=0.38)
        self.entry_nome = Entry(self.f1)
        self.entry_nome.place(relx=0.11, rely=0.48, relwidth=0.35, relheight=0.1)
        # label e entry email
        self.label_email = Label(self.f1, text='Email', fg='#4682B4', bg='#F0F8FF', font=('arial', 14, 'bold'))
        self.label_email.place(relx=0.54, rely=0.38)
        self.entry_email = Entry(self.f1)
        self.entry_email.place(relx=0.54, rely=0.48, relwidth=0.35, relheight=0.1)
        # label e entry telefone
        self.label_fone = Label(self.f1, text='Telefone', fg='#4682B4', bg='#F0F8FF', font=('arial', 14, 'bold'))
        self.label_fone.place(relx=0.11, rely=0.65)
        self.entry_fone = Entry(self.f1)
        self.entry_fone.place(relx=0.11, rely=0.75, relwidth=0.35, relheight=0.1)
        # label e entry cidade
        self.label_cidade = Label(self.f1, text='Cidade', fg='#4682B4', bg='#F0F8FF', font=('arial', 14, 'bold'))
        self.label_cidade.place(relx=0.54, rely=0.65)
        self.entry_cidade = Entry(self.f1)
        self.entry_cidade.place(relx=0.54, rely=0.75, relwidth=0.35, relheight=0.1)

    def lista_frame2(self) -> None:
        self.listaCLI = ttk.Treeview(self.f2, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.listaCLI.heading('#0', text='')
        self.listaCLI.heading('#1', text='Código')
        self.listaCLI.heading('#2', text='Nome')
        self.listaCLI.heading('#3', text='Email')
        self.listaCLI.heading('#4', text='Telefone')
        self.listaCLI.heading('#5', text='Cidade')

        self.listaCLI.column('#0', width=0)
        self.listaCLI.column('#1', width=50)
        self.listaCLI.column('#2', width=200)
        self.listaCLI.column('#3', width=200)
        self.listaCLI.column('#4', width=200)
        self.listaCLI.column('#5', width=200)

        self.listaCLI.place(relx=0.0, rely=0.0, relwidth=0.98, relheight=0.99)

        self.scroolB = Scrollbar(self.f2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroolB.set)
        self.scroolB.place(relx=0.98, relwidth=0.02, relheight=0.99)

TelaGUI()

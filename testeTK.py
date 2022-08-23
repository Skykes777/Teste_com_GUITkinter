from tkinter import *

class Aplication():
    def __init__(self) -> None:
        self.janela = Tk()
        self.Tela()
        self.Textos()
        self.janela.mainloop()

    def Tela(self) -> None:
        self.janela.title('Teste de Janela TKinter')
        self.janela.configure(background='#483D8B')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=980, height=700)
        self.janela.minsize(width=400, height=300)

    def Textos(self) -> None:
        f1 = Frame(self.janela)
        f2 = Frame(self.janela)
        texto1 = Label(f1, text='Mensagem de teste no topo(top)', bg='black', fg='white', height='5', width=980)
        texto2 = Label(f2, text='Mensagem de teste na parte de baixo(bottom)', bg='red', fg='white', height='5', width=970)

        f1.pack(side='top')
        f2.pack(side='bottom')
        texto1.pack(fill=X)
        texto2.pack(fill=X)

Aplication()

from tkinter import *

class Aplication():
    def __init__(self) -> None:
        self.janela = Tk()
        self.Tela()
        self.Frames_de_tela()
        self.botoes()
        self.janela.mainloop()

    def Tela(self) -> None:
        self.janela.title('Teste de Janela TKinter')
        self.janela.configure(background='#483D8B')
        self.janela.geometry('800x600')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=980, height=700)
        self.janela.minsize(width=400, height=300)

    def Frames_de_tela(self):
        self.frame_1 = Frame(self.janela, bg='#F0F8FF', highlightbackground='#B0E0E6', highlightthickness=4)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.janela, bg='#F0F8FF', highlightbackground='#B0E0E6', highlightthickness=4)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def botoes(self) -> None:
        self.bt_limpar = Button(self.frame_1, text='Limpar')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text='Buscar')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text='Novo')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text='Alterar')
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text='Apagar')
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
 
Aplication()

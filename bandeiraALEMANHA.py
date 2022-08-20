from tkinter import *

class BandeiraAlemanha:
    def __init__(self) -> None:
        self.bandeira = Tk()
        self.bandeira.title('ALEMANHA')
        self.f1 = Frame(self.bandeira, bg='black', height='120', width=600)
        self.f2 = Frame(self.bandeira, bg='red', height='120', width=600)
        self.f3 = Frame(self.bandeira, bg='yellow', height='120', width=600)

        self.f1.pack(side='top')
        self.f2.pack(side='top')
        self.f3.pack(side='top')

        self.bandeira.mainloop()

babG = BandeiraAlemanha()

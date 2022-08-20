from tkinter import *

class BandeiraRussia:
    def __init__(self) -> None:
        self.bandeira = Tk()
        self.bandeira.title('RUSSIA')
        self.f1 = Frame(self.bandeira, bg='white', height='120', width=600)
        self.f2 = Frame(self.bandeira, bg='blue', height='120', width=600)
        self.f3 = Frame(self.bandeira, bg='red', height='120', width=600)

        self.f1.pack(side='top')
        self.f2.pack(side='top')
        self.f3.pack(side='top')

        self.bandeira.mainloop()

banR = BandeiraRussia()

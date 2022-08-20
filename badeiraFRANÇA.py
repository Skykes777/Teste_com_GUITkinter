from tkinter import *

class BandeiraFrança:
    def __init__(self) -> None:
        self.bandeira = Tk()
        self.bandeira.title('FRANÇA')
        self.f1 = Frame(self.bandeira, bg='blue', height='350', width=200)
        self.f2 = Frame(self.bandeira, bg='white', height='350', width=200)
        self.f3 = Frame(self.bandeira, bg='red', height='350', width=200)
    
        self.f1.pack(side='left')
        self.f2.pack(side='left')
        self.f3.pack(side='left')

        self.bandeira.mainloop()

banF = BandeiraFrança()

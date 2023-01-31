from tkinter import *
from prideti_langas import Prideti

class Main_langas:
    def __init__(self, langas):
        self.langas = langas
        self.f_paeiska = Frame(self.langas)
        self.f_status = Frame(self.langas)
        self.l_paieska = Label(self.f_paeiska, text="Iveskite ieskomo kliento varda ir pavarde")
        self.e_paieska = Entry(self.f_paeiska, relief=SUNKEN, border=5)
        self.b_paieska = Button(self.f_paeiska, border=5, text="Enter", command=NONE) #TODO Ivesti komanda
        self.b_prideti = Button(self.f_paeiska, border=5, text="Add New", command=self.run_prideti_langas)
        status = Label(langas, text="Laukiam veiksmo", relief=SUNKEN, border=1, wraplength=200, justify=CENTER)


        self.f_paeiska.pack()
        
        # self.l_paieska.pack(side=TOP)
        # self.e_paieska.pack(side=TOP)
        # self.b_paieska.pack(side=TOP)
        self.l_paieska.grid(sticky=N, column=1, row=1)
        self.e_paieska.grid(sticky=N, column=1, row=2)
        self.b_paieska.grid(sticky=N, column=2, row=2)
        self.b_prideti.grid(sticky=S, column=2)
        status.pack(side=BOTTOM, fill=X)

        

    def run_prideti_langas(self):
        self.prideti_langas = Toplevel(self.langas)
        self.app = Prideti(self.prideti_langas)
        

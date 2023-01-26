from tkinter import *

class Prideti:

    def __init__(self, prideti):
        self.prideti = prideti
        self.prideti.title("Prideti naujus duomenis")
        self.f_main = Frame(self.prideti)
        self.f_prideti = Frame(self.prideti)
        self.l_prideti = Label(self.f_prideti, text="Iveskite ieskomo kliento arba pirkinio id")
        self.e_prideti = Entry(self.f_prideti, relief=SUNKEN, border=5)
        self.b_prideti = Button(self.f_prideti, border=5, text="Enter", command=NONE) #TODO Ivesti komanda      

        self.f_prideti.pack()
        self.l_prideti.grid(sticky=N, column=1, row=1)
        self.e_prideti.grid(sticky=N, column=1, row=2)
        self.b_prideti.grid(sticky=N, column=2, row=2)
        
        
        self.prideti.mainloop()
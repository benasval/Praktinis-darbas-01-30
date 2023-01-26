from tkinter import *
from main_langas import Main_langas

def run_langas():
    langas = Tk()
    langas.geometry("270x120")
    langas.title("Langas su klasem")
    app = Main_langas(langas)
    langas.mainloop() 

if __name__ == "__main__":
    run_langas()

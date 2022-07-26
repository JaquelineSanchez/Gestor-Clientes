""" Menú gráfico"""
from tkinter import *

class CenterMixin:

    def center(self):
        """ Centrar la ventana"""
        self.update()
        w = self.winfo_width()  #ancho de ventana        
        h = self.winfo_height() #altura de ventana
        ws = self.winfo_screenwidth() #ancho de monitor
        hs = self.winfo_screenheight() #altura de monitor
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        #WIDTH x HEIGHT + OFFSET_X + OFFSET_Y
        self.geometry(f"{w}x{h}+{x}+{y}")


class Main(Tk, CenterMixin):
    
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()
    
    def build(self):
        button = Button(self,text = "Hola", command = self.hola)
        button.pack()

    def hola(self):
        print("Hola mundo!")

if __name__ == "__main__":
    app = Main()
    app.mainloop()
""" Menú gráfico"""
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

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
        frame = Frame(self)
        frame.pack()
        
        #Configurar tabla
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI','NOMBRE','APELLIDO')        

        treeview.column("#0",width=0,stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("NOMBRE", anchor=CENTER)
        treeview.column("APELLIDO", anchor=CENTER)

        treeview.heading("DNI",text="DNI", anchor=CENTER)
        treeview.heading("NOMBRE",text="NOMBRE", anchor=CENTER)
        treeview.heading("APELLIDO",text="APELLIDO", anchor=CENTER)
        
        #añadir scroll
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)        
        treeview['yscrollcommand'] = scrollbar.set

        #cargar informacion
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index ='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))
        treeview.pack()

        #botones
        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame,text="Crear",command=None).grid(row=0,column=0)
        Button(frame,text="Modificar",command=None).grid(row=0,column=1)
        Button(frame,text="Borrar",command=self.borrar).grid(row=0,column=2)

        #atributo de instancia
        self.treeview = treeview
    
    def borrar(self):
        cliente = self.treeview.focus()
        if cliente:
            #lista con sus valores
            campos = self.treeview.item(cliente,'values')
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar a {campos[1]} {campos[2]}?",
                icon=WARNING)
            if confirmar:
                self.treeview.delete(cliente)



if __name__ == "__main__":
    app = Main()
    app.mainloop()
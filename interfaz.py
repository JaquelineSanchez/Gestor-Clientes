""" Menú gráfico"""
import database as db
import auxiliares
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

#Creacion de subventana
class CreateClientWindow(Toplevel, CenterMixin):

    def __init__(self, parent):
        #indicar quien es padre de la subventana
        super().__init__(parent)
        self.title("Crear un cliente")
        self.build()
        self.center()
        #Obligan a realizar una accion en la subventana antes de regresar a la otra
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20,pady=10)

        Label(frame,text="DNI (2 int y 1 char):").grid(row=0,column=0)
        Label(frame,text="Nombre (2 - 30 chars):").grid(row=1,column=0)
        Label(frame,text="Apellido (2 - 30 chars):").grid(row=2,column=0)

        dni = Entry(frame)
        dni.grid(row=0,column=1)
        #Configurar evento para validar datos
        dni.bind("<KeyRelease>", lambda event: self.validar(event, 0))
        nombre = Entry(frame)
        nombre.grid(row=1,column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validar(event, 1))
        apellido = Entry(frame)    
        apellido.grid(row=2,column=1)
        apellido.bind("<KeyRelease>", lambda event: self.validar(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Crear", command=self.crearCliente)
        crear.configure(state=DISABLED)
        crear.grid(row=0,column=0)
        self.crear = crear
        Button(frame, text="Cancelar", command=self.cerrar).grid(row=0,column=1)        

        self.validaciones = [0, 0, 0]
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def crearCliente(self):
        #master = ventana principal
        self.master.treeview.insert(
            parent='', index ='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        self.cerrar()

    def validar(self, event, index):
        valor = event.widget.get()
        valido = auxiliares.validarDni(valor, db.Clientes.lista) if index == 0 \
            else valor.isalpha() and (2 <= len(valor) <= 30)
        event.widget.configure({"bg":"Green" if valido else "Red"})
        #Cambiar estado del boton
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)

        

    def cerrar(self):
        self.destroy()
        self.update()


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

        Button(frame,text="Crear",command=self.crear).grid(row=0,column=0)
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

    def crear(self):
        CreateClientWindow(self)

if __name__ == "__main__":
    app = Main()
    app.mainloop()
class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido= apellido

    def __str__(self):
        return "({}) {} {}".format(self.dni, self.nombre, self.apellido)

class Clientes:

    lista = []

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Cliente.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar(dni,nombre, apellido):        
        for i,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].nombre = apellido
                return Clientes.lista[i]

    @staticmethod
    def borrar(dni):
        for i,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(i)


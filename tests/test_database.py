import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('19J','Jose','Sanchez'),
            db.Cliente('45S','Saul','Ramirez'),
            db.Cliente('25A','Ana','Bocanegra')
        ]

    def test_BuscarCliente(self):
        clienteExis = db.Clientes.buscar('45S')
        clienteInex = db.Clientes.buscar('69X')
        self.assertIsNotNone(clienteExis)
        self.assertIsNone(clienteInex)    

#cmd: pytest -v
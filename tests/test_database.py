import auxiliares
import copy
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

    def test_crearCliente(self):
        nuevoC = db.Clientes.crear('39X','Hector','Costa')        
        self.assertEqual(nuevoC.apellido,'Costa')
        self.assertEqual(nuevoC.dni,'39X')
        self.assertEqual(nuevoC.nombre,'Hector')    
        self.assertEqual(len(db.Clientes.lista),4)

    def test_modificarCliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('25A'))
        cliente_modificado = db.Clientes.modificar('25A','Mary','Luna')
        self.assertEqual(cliente_a_modificar.nombre,'Ana')
        self.assertEqual(cliente_modificado.nombre,'Mary')

    def test_borrarCliente(self):
        clienteBorrado = db.Clientes.borrar('45S')
        clienteInex = db.Clientes.buscar('45S')
        self.assertEqual(clienteBorrado.dni,'45S')
        self.assertIsNone(clienteInex)

    def test_validarDni(self):
        self.assertTrue(auxiliares.validarDni('00A',db.Clientes.lista))
        self.assertFalse(auxiliares.validarDni('A00',db.Clientes.lista))
        self.assertFalse(auxiliares.validarDni('19J',db.Clientes.lista))

#cmd: pytest -v
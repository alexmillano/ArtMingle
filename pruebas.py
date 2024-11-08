import unittest
from controlador.usuarioControlador import UsuarioControlador


class Pruebas(unittest.TestCase):

    def test_iniciarsesion_verdadero(self):
        controlador = UsuarioControlador()
        resultado = controlador.iniciarSesion("prueba@gmail.com", "123")
        self.assertTrue(resultado)  


    def test_iniciarsesion_falso(self):
        controlador = UsuarioControlador()
        resultado = controlador.iniciarSesion("noexiste", "noexiste")
        self.assertFalse(resultado)  


if __name__ == '__main__':
    unittest.main()
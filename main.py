from modelo.usuarios.usuarioModelo import UsuarioModelo
from controlador.usuarioControlador import Usuario
from vista.inicio_sesion import iniciar_sesion
from modelo.conexion import Conexion

conexion=Conexion()#No tocar


#usuario_controlador.crear_tabla_usuario()
#usuario_controlador.insertar_usuario("Prueba", "Prueba", "prueba@gmail.com" , 99999999, "prueba1", "123","","Biografia prueba")

iniciar_sesion()


conexion.cerrar_conexion()#No tocar
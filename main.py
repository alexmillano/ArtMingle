from modelo.usuarios.usuarioModelo import UsuarioControlador
from modelo.conexion import Conexion

base_datos="artmingle.db"
conexion=Conexion(base_datos)

usuario_controlador = UsuarioControlador(conexion)

#usuario_controlador.crear_tabla_usuario()
#usuario_controlador.insertar_usuario("Prueba", "Prueba", "prueba@gmail.com" , 99999999, "prueba1", "123","","Biografia prueba")

usuario_controlador.mostrar_usuarios()


conexion.cerrar_conexion
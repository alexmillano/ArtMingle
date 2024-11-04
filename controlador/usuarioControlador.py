from modelo.usuario.usuario import Usuario
from modelo.conexion import Conexion

class UsuarioControlador:

    def iniciarSesion(self,email,contrasena):
        nueva_conexion=Conexion()
        usuario_modelo=Usuario(nueva_conexion)
        respuesta=usuario_modelo.iniciar_sesion(email,contrasena)

        if respuesta:
            nueva_conexion.cerrar_conexion()
            return print("Inicio sesion")
        
        else:
            nueva_conexion.cerrar_conexion()
            return print("Error al iniciar sesion")




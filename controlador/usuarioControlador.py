from modelo.usuario.usuario import Usuario
from modelo.conexion import Conexion

class UsuarioControlador:

    def iniciarSesion(self,email,contrasena):
        nueva_conexion=Conexion()
        usuario_modelo=Usuario(nueva_conexion)
        respuesta=usuario_modelo.iniciar_sesion(email,contrasena)

        if respuesta:
            nueva_conexion.cerrar_conexion()
            print("Inicio sesion")
            return True
        
        else:
            nueva_conexion.cerrar_conexion()
            print("Error al iniciar sesion")
            return False
        

    def registrarse(self, nombre, apellido, correo, telefono, nombre_usuario, contrasena, foto_perfil, biografia):
        





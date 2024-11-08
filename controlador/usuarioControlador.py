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
        nueva_conexion=Conexion()
        usuario_modelo=Usuario(nueva_conexion)
        respuesta=usuario_modelo.insertar_usuario(nombre, apellido, correo, telefono, nombre_usuario, contrasena, foto_perfil, biografia)

        if respuesta:
            nueva_conexion.cerrar_conexion()
            print("Usuario Creado")
            return True
        
        else:
            nueva_conexion.cerrar_conexion()
            print("Error al crear usuario")
            return False

    
        
    def validarUsuario(self,usuario,correo):
        nueva_conexion=Conexion()
        usuario_modelo=Usuario(nueva_conexion)

        respuesta=usuario_modelo.verificar_usuarioycorreo(usuario,correo)

        if respuesta=="correo":
            print("El correo ya esta en uso")
            nueva_conexion.cerrar_conexion()
            return "correo"
        elif respuesta=="usuario":
            print("El nombre de usuario ya esta en uso")
            nueva_conexion.cerrar_conexion()
            return "usuario"
        else:
            nueva_conexion.cerrar_conexion()
            return True

        





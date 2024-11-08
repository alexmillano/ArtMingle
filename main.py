from modelo.usuario.usuario import Usuario
from controlador.usuarioControlador import UsuarioControlador
from vista.inicio_sesion import iniciar_sesion
from modelo.conexion import Conexion
from modelo.contenido.contenido import Contenido
from controlador.contenidoControlador import ContenidoControlador
from vista.subir_contenido import subir_contenido


conexion=Conexion()#No tocar


#usuario=Usuario(conexion)
#usuario.crear_tabla_usuario()
#usuario.insertar_usuario("Prueba", "Prueba", "prueba@gmail.com" , 99999999, "prueba1", "123","","Biografia prueba")
#usuario.mostrar_usuarios()

iniciar_sesion()

conexion.cerrar_conexion()#No tocar



#python -m unittest pruebas.py
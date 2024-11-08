from modelo.contenido.contenido import Contenido
from modelo.conexion import Conexion

class ContenidoControlador:
    def __init__(self, conexion):
        self.contenido_modelo = Contenido(conexion=conexion)

    def crear_tabla_si_no_existe(self):
        self.contenido_modelo.crear_tabla_contenido()

    def agregar_contenido(self, titulo, descripcion, fecha_carga, likes, comentario, url_video, url_imagen, id_usuario):
        try:
            contenido = self.contenido_modelo.insertar_contenido(
                titulo, descripcion, fecha_carga, likes, comentario, url_video, url_imagen, id_usuario
            )
            return contenido
        except Exception as e:
            print(f"Error en el controlador al agregar contenido: {e}")
            return None

    def obtener_contenidos(self):
        return self.contenido_modelo.mostrar_contenido()

    def editar_contenido(self, titulo, descripcion, url_imagen, url_video, id_usuario):
        try:
            self.contenido_modelo.editar_contenido(titulo, descripcion, url_imagen, url_video, id_usuario)
            print("Contenido editado con éxito.")
        except Exception as e:
            print(f"Error al editar contenido en el controlador: {e}")

    def eliminar_contenido(self, id_contenido):
        try:
            self.contenido_modelo.eliminar_contenido(id_contenido)
            print("Contenido eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar contenido en el controlador: {e}")

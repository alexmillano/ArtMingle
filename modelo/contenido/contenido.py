from ..conexion import Conexion
from datetime import datetime

class Contenido:
    def __init__(self, idContenido=None,titulo="",descripcion="",fechaCarga=None,comentario="",urlVideo=None,urlImagen=None,idUsuario=None,conexion=None):
        self.idContenido=idContenido
        self.titulo=titulo
        self.descripcion=descripcion
        self.fechaCarga=fechaCarga
        self.like=0
        self.comentario=comentario
        self.urlVideo=urlVideo
        self.urlImagen=urlImagen
        self.idUsuario=idUsuario
        self.conexion=conexion

    def get_idContenido(self):
        return self.idContenido

    def set_idContenido(self, idContenido):
        self.idContenido = idContenido

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def get_fechaCarga(self):
        return self.fechaCarga

    def set_fechaCarga(self, fechaCarga):
        self.fechaCarga = fechaCarga

    def get_like(self):
        return self.like

    def set_like(self, like):
        self.like = like

    def get_comentario(self):
        return self.comentario

    def set_comentario(self, comentario):
        self.comentario = comentario

    def get_urlVideo(self):
        return self.urlVideo

    def set_urlVideo(self, urlVideo):
        self.urlVideo = urlVideo

    def get_urlImagen(self):
        return self.urlImagen

    def set_urlImagen(self, urlImagen):
        self.urlImagen = urlImagen

    def get_idUsuario(self):
        return self.idUsuario

    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def crear_tabla_contenido(self):
        cursor = self.conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contenidos (id_Contenido INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descripcion TEXT NOT NULL, fechaCarga TEXT NOT NULL DEFAULT CURRENT_DATE, like  INT DEFAULT 0, comentario TEXT NOT NULL, urlVideo TEXT NOT NULL UNIQUE, urlImagen TEXT NOT NULL UNIQUE, idUsuario INTEGER NOT NULL )")
        print("Tabla contenidos creada")
        self.conexion.commit()

    def insertar_contenido(self, titulo, descripcion, fechaCarga, like, comentario, urlVideo, urlImagen, idUsuario):

        try:     
            self.conexion.cursor.execute(
                '''
                INSERT INTO contenidos (
                    titulo, descripcion, fechaCarga, like, comentario, urlVideo, urlImagen, idUsuario
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', 
                (titulo, descripcion, fechaCarga, like, comentario, urlVideo, urlImagen, idUsuario)
            )    
            print("Contenido insertado")

            idContenido = self.conexion.cursor.lastrowid
            contenido_creado=Contenido(idContenido,titulo,descripcion,fechaCarga,like,comentario,urlVideo,urlImagen,idUsuario)
            self.conexion.commit()
            return contenido_creado

        except Exception  as e:
            print("Error al insertar contenido:", e)

    def mostrar_contenido(self):
        self.conexion.cursor.execute("SELECT * FROM contenidos")
        contenidos= self.conexion.cursor.fetchall()
        for fila in contenidos:
            print(fila) 

    def editar_contenido(self, titulo, descripcion, urlImagen, urlVideo, idUsuario):
        self.conexion.cursor.execute(
            "UPDATE contenidos SET titulo=?, descripcion=?, urlImagen=?, urlVideo=? WHERE idUsuario=?", 
            (titulo, descripcion, urlImagen, urlVideo,idUsuario)
        )
        self.conexion.commit()

    def eliminar_contenido(self, idContenido):
        try :
            self.conexion.cursor.execute("DELETE FROM contenidos WHERE id_Contenido=?", (idContenido,))
            self.conexion.commit()
            print("Contenido eliminado")
        except Exception  as e:
            print("Error al eliminar el contenido:", e)

    
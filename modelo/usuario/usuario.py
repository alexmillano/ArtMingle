from ..conexion import Conexion
from datetime import datetime

class Usuario:
    #EstoNO MODIFICAR
    def __init__(self,conexion=None, idUsuario=None,nombre="", apellido="", correo="", telefono=None, usuario="", clave="", biografia="", foto=None):
        self.conexion = conexion
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecharegistro = None
        self.correo = correo
        self.telefono = telefono
        self.usuario = usuario
        self.clave = clave
        self.seguidores = 0
        self.seguidos = 0
        self.foto = foto
        self.biografia = biografia


    def get_idUsuario(self):
        return self.idUsuario

    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_fecharegistro(self):
        return self.fecharegistro

    def set_fecharegistro(self, fecharegistro):
        self.fecharegistro = fecharegistro

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_clave(self):
        return self.clave

    def set_clave(self, clave):
        self.clave = clave

    def get_seguidores(self):
        return self.seguidores

    def set_seguidores(self, seguidores):
        self.seguidores = seguidores

    def get_seguidos(self):
        return self.seguidos

    def set_seguidos(self, seguidos):
        self.seguidos = seguidos

    def get_foto(self):
        return self.foto

    def set_foto(self, foto):
        self.foto = foto

    def get_biografia(self):
        return self.biografia

    def set_biografia(self, biografia):
        self.biografia = biografia

    def crear_tabla_usuario(self):
        self.conexion.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL, fecha_registro TEXT NOT NULL DEFAULT CURRENT_DATE, correo TEXT NOT NULL UNIQUE, telefono INTEGER NOT NULL, nombre_Usuario TEXT NOT NULL UNIQUE, contrasena TEXT NOT NULL,  seguidores INT DEFAULT 0, seguidos INT DEFAULT 0, foto_Perfil BLOB , biografia TEXT NOT NULL)")
        print("Tabla usuario creada")
        self.conexion.conexion.commit()


    def insertar_usuario(self, nombre, apellido, correo, telefono, nombre_usuario, contrasena, foto_perfil, biografia):

        try:     
            self.conexion.cursor.execute(
                '''
                INSERT INTO usuarios (
                    nombre, apellido,  correo, telefono, nombre_Usuario, contrasena, foto_Perfil, biografia
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', 
                (nombre, apellido, correo, telefono, nombre_usuario, contrasena,foto_perfil, biografia)
            )    
            print("Usuario insertado")

            id_usuario = self.conexion.cursor.lastrowid
            usuario_creado=Usuario(id_usuario,nombre, apellido, correo, telefono,contrasena, foto_perfil, biografia)
            self.conexion.conexion.commit()
            return usuario_creado

        except Exception  as e:
            print("Error al insertar usuario:", e)


    def mostrar_usuarios(self):
        self.conexion.cursor.execute("SELECT * FROM usuarios")
        usuarios= self.conexion.cursor.fetchall()
        for fila in usuarios:
            print(fila) 


    def editar_usuario(self, dni, nombre, usuario, rol):
        self.conexion.cursor.execute(
            "UPDATE usuarios SET nombre=?, usuario=?, rol=? WHERE dni=?", 
            (nombre, usuario, rol, dni)
        )
        self.conexion.conexion.commit()

    def eliminar_usuario(self, idUsuario):
        try :
            self.conexion.cursor.execute("DELETE FROM usuarios WHERE id_Usuario=?", (idUsuario,))
            self.conexion.conexion.commit()
            print("Usuario eliminado")
        except Exception  as e:
            print("Error al eliminar el usuario:", e)


    def iniciar_sesion(self, correo, contrasena):
        try:
            self.conexion.cursor.execute("SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?", (correo, contrasena))
            usuario = self.conexion.cursor.fetchone()
            return usuario
        except Exception  as e:
            print("Error al buscar mail y contraseña:", e)



    def verificar_usuarioycorreo(self, nombre_usuario,correo):
        self.conexion.cursor.execute("SELECT * FROM usuarios WHERE nombre_Usuario = ? OR correo = ?", (nombre_usuario, correo))
        usuario_existente = self.conexion.cursor.fetchone()

        if usuario_existente:
            if usuario_existente[6] == nombre_usuario:  
                return "usuario"  
            if usuario_existente[4] == correo:  
                return "correo"           
        else:
            return True 



    """" POR SI HAY QUE MODIFICAR ALGO EN LA TABLA, LA BORRA Y LA VUELVE A CREAR 
    """
    def recrear_tabla_usuarios(self):
        self.cursor.execute("DROP TABLE IF EXISTS usuarios")
        print("Tabla usuario eliminada")
        self.conexion.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL, fecha_registro TEXT NOT NULL DEFAULT CURRENT_DATE, correo TEXT NOT NULL UNIQUE, telefono INTEGER NOT NULL, nombre_Usuario TEXT NOT NULL UNIQUE, contrasena TEXT NOT NULL,  seguidores INT DEFAULT 0, seguidos INT DEFAULT 0, foto_Perfil BLOB , biografia TEXT NOT NULL)")
        print("Tabla usuario creada nuevamente")
        self.conexion.commit()
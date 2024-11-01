from ..conexion import Conexion
from datetime import datetime

class UsuarioModelo:
    def __init__(self, conexion):
        self.conexion = conexion


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
            self.conexion.conexion.commit()

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

    def eliminar_usuario(self, dni):
        self.conexion.cursor.execute("DELETE FROM usuarios WHERE dni=?", (dni))
        self.conexion.conexion.commit()


    def iniciar_sesion(self, correo, contrasena):
        try:
            self.conexion.cursor.execute("SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?", (correo, contrasena))
            usuario = self.conexion.cursor.fetchone()
            return usuario
        except Exception  as e:
            print("Error al buscar mail y contraseña:", e)



    """" POR SI HAY QUE MODIFICAR ALGO EN LA TABLA, LA BORRA Y LA VUELVE A CREAR 
    """
    def recrear_tabla_usuarios(self):
        self.cursor.execute("DROP TABLE IF EXISTS usuarios")
        print("Tabla usuario eliminada")
        self.conexion.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL, fecha_registro TEXT NOT NULL DEFAULT CURRENT_DATE, correo TEXT NOT NULL UNIQUE, telefono INTEGER NOT NULL, nombre_Usuario TEXT NOT NULL UNIQUE, contrasena TEXT NOT NULL,  seguidores INT DEFAULT 0, seguidos INT DEFAULT 0, foto_Perfil BLOB , biografia TEXT NOT NULL)")
        print("Tabla usuario creada nuevamente")
        self.conexion.commit()
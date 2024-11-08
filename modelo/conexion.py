import sqlite3

class Conexion:
    def __init__(self):
        self.nombre_bd = "artmingle.db"
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

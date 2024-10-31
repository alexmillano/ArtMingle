from ..modelo.usuarios.usuarioModelo import UsuarioModelo

class Usuario:
    def __init__(self, idUsuario, nombre, apellido, fecharegistro, correo, telefono, usuario, clave, seguidores, seguidos, foto, biografia):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecharegistro = fecharegistro
        self.correo = correo
        self.telefono = telefono
        self.usuario = usuario
        self.clave = clave
        self.seguidores = seguidores
        self.seguidos = seguidos
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

    


    #def iniciarSesion(email,contrasena):

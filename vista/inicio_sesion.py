import tkinter as tk
from controlador.usuarioControlador import UsuarioControlador

def iniciar_sesion():
    usuario_controlador = UsuarioControlador()

    root = tk.Tk()
    root.title("Iniciar sesión")

    email_label = tk.Label(root, text="Ingrese su email")
    email_label.pack()
    email_entrada = tk.Entry(root)
    email_entrada.pack()

    contrasena_label = tk.Label(root, text="Ingrese su contraseña")
    contrasena_label.pack()
    contrasena_entrada = tk.Entry(root, show="*")
    contrasena_entrada.pack()

    mensaje_error = None

    def evento_boton_iniciar_sesion():
        nonlocal mensaje_error
        respuesta = usuario_controlador.iniciarSesion(email_entrada.get(), contrasena_entrada.get())

        if not respuesta and mensaje_error is None:
            mensaje_error = tk.Label(root, text="Datos incorrectos", fg="red")
            mensaje_error.pack()

    def evento_boton_registrarse():
        from vista.registrarse import registrarse
        root.destroy()
        registrarse()
        

    boton_iniciar_sesion = tk.Button(root, text="Ingresar", command=evento_boton_iniciar_sesion)
    boton_iniciar_sesion.pack()
    boton_registrarse = tk.Button(root, text="Registrarse", command=evento_boton_registrarse)
    boton_registrarse.pack()

    root.mainloop()
import tkinter as tk;
from controlador.usuarioControlador import Usuario

def iniciar_sesion():
    usuario_controlador = Usuario()

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

    def evento_boton():
        usuario_controlador.iniciarSesion(email_entrada.get(), contrasena_entrada.get())

    boton = tk.Button(root, text="Ingresar", command=evento_boton)
    boton.pack()

    root.mainloop()
import tkinter as tk
from controlador.usuarioControlador import UsuarioControlador
from vista.paginainicio import paginainicio

def iniciar_sesion():
    usuario_controlador = UsuarioControlador()

    root = tk.Tk()
    root.title("ArtMingle - Iniciar sesión")
    root.geometry("900x900")  
    root.config(bg="#f8f8f8") 

    title_label = tk.Label(root, text="Bienvenido a ArtMingle", font=("Brush Script MT", 28, "bold"), bg="#f8f8f8", fg="#ff6347")
    title_label.pack(pady=30)


    email_label = tk.Label(root, text="Ingrese su email", font=("Comic Sans MS", 16), bg="#f8f8f8", fg="#333")
    email_label.pack(pady=10)
    email_entrada = tk.Entry(root, font=("Comic Sans MS", 14), width=40, bd=2, relief="solid", bg="#fff", fg="#333")
    email_entrada.pack(pady=15)

    contrasena_label = tk.Label(root, text="Ingrese su contraseña", font=("Comic Sans MS", 16), bg="#f8f8f8", fg="#333")
    contrasena_label.pack(pady=10)
    contrasena_entrada = tk.Entry(root, font=("Comic Sans MS", 14), width=40, bd=2, relief="solid", bg="#fff", fg="#333", show="*")
    contrasena_entrada.pack(pady=15)


    mensaje_error = None

    def evento_boton_iniciar_sesion():
        nonlocal mensaje_error
        respuesta = usuario_controlador.iniciarSesion(email_entrada.get(), contrasena_entrada.get())

        if not respuesta:
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="Datos incorrectos", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 14, "italic"))
            mensaje_error.pack(pady=10)
        else:
            root.destroy()
            paginainicio() 


    boton_iniciar_sesion = tk.Button(root, text="Ingresar", command=evento_boton_iniciar_sesion, font=("Comic Sans MS", 14), bg="#ff6347", fg="white", width=20, height=2, bd=0, relief="solid", activebackground="#e74c3c")
    boton_iniciar_sesion.pack(pady=30)

    def evento_boton_registrarse():
        from vista.registrarse import registrarse
        root.destroy()
        registrarse()

    boton_registrarse = tk.Button(root, text="Registrarse", command=evento_boton_registrarse, font=("Comic Sans MS", 14), bg="#4CAF50", fg="white", width=20, height=2, bd=0, relief="solid", activebackground="#2ecc71")
    boton_registrarse.pack(pady=20)

    root.mainloop()
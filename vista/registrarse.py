import tkinter as tk
from controlador.usuarioControlador import UsuarioControlador
from tkinter import filedialog

def registrarse():
    usuario_controlador = UsuarioControlador()

    root = tk.Tk()
    root.title("ArtMingle - Registrarse")
    root.geometry("900x900") 
    root.config(bg="#f8f8f8") 

    title_label = tk.Label(root, text="Crea tu cuenta en ArtMingle", font=("Brush Script MT", 14, "bold"), bg="#f8f8f8", fg="#ff6347")
    title_label.pack(pady=15)

    nombre = tk.Label(root, text="Nombre", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    nombre.pack()
    nombre_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    nombre_entrada.pack(pady=5)

    apellido = tk.Label(root, text="Apellido", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    apellido.pack()
    apellido_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    apellido_entrada.pack(pady=5)

    email = tk.Label(root, text="Ingrese su email", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    email.pack()
    email_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    email_entrada.pack(pady=5)

    telefono = tk.Label(root, text="Ingrese su teléfono", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    telefono.pack()
    telefono_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    telefono_entrada.pack(pady=5)
    
    usuario = tk.Label(root, text="Ingrese su usuario", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    usuario.pack()
    usuario_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    usuario_entrada.pack(pady=5)

    contrasena_label = tk.Label(root, text="Ingrese su contraseña", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    contrasena_label.pack()
    contrasena_entrada = tk.Entry(root, show="*", font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    contrasena_entrada.pack(pady=5)

    foto = tk.Label(root, text="Ingrese su foto de perfil", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    foto.pack(pady=10)

    foto_blob = None

    def seleccionar_imagen():
        nonlocal foto_blob
        ruta_imagen = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if ruta_imagen:
            with open(ruta_imagen, 'rb') as archivo_imagen:
                foto_blob = archivo_imagen.read()

    boton_seleccionar_imagen = tk.Button(root, text="Seleccionar Imagen", command=seleccionar_imagen, font=("Comic Sans MS", 10), bg="#4CAF50", fg="white", width=18, height=1, bd=0, relief="solid", activebackground="#2ecc71")
    boton_seleccionar_imagen.pack(pady=8)

    biografia = tk.Label(root, text="Ingrese su biografía", font=("Comic Sans MS", 10), bg="#f8f8f8", fg="#333")
    biografia.pack()
    biografia_entrada = tk.Entry(root, font=("Comic Sans MS", 10), width=25, bd=1, relief="solid", bg="#fff", fg="#333")
    biografia_entrada.pack(pady=5)

    mensaje_error = None
    def evento_boton_registrarse():
        nonlocal mensaje_error

        if not nombre_entrada.get() or not apellido_entrada.get() or not email_entrada.get() or not telefono_entrada.get() or not usuario_entrada.get() or not contrasena_entrada.get() or not biografia_entrada.get():
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="Todos los campos son obligatorios.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)
            return


        if not telefono_entrada.get().isdigit():
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="El teléfono solo debe contener números.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)
            return
        
        if "@" not in email_entrada.get():
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="El correo debe contener '@'.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)
            return

        
        validar_usuarioycorreo = usuario_controlador.validarUsuario(usuario_entrada.get(), email_entrada.get())
        if validar_usuarioycorreo == "correo":
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="Su correo ya tiene una cuenta activa", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)
            return
        elif validar_usuarioycorreo == "usuario":
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="Su nombre de usuario ya está en uso", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)
            return

        respuesta = usuario_controlador.registrarse(nombre_entrada.get(), apellido_entrada.get(), email_entrada.get(),telefono_entrada.get(), usuario_entrada.get(),contrasena_entrada.get(), foto_blob, biografia_entrada.get())

        if respuesta:
            mensaje_error = tk.Label(root, text="Usuario creado.", fg="green", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            root.destroy()
            from vista.inicio_sesion import iniciar_sesion
            iniciar_sesion()
        else:
            mensaje_error = tk.Label(root, text="No se pudo crear el usuario.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 10, "italic"))
            mensaje_error.pack(pady=5)

    boton_registrarse = tk.Button(root, text="Registrarse", command=evento_boton_registrarse, font=("Comic Sans MS", 10), bg="#ff6347", fg="white", width=18, height=1, bd=0, relief="solid", activebackground="#e74c3c")
    boton_registrarse.pack(pady=10)

    def evento_boton_atras():
        from vista.inicio_sesion import iniciar_sesion
        root.destroy()
        iniciar_sesion()

    boton_atras = tk.Button(root, text="Atras", command=evento_boton_atras, font=("Comic Sans MS", 10), bg="#4CAF50", fg="white", width=18, height=1, bd=0, relief="solid", activebackground="#2ecc71")
    boton_atras.pack(pady=5)

    root.mainloop()
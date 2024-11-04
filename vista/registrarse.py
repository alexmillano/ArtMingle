import tkinter as tk
from controlador.usuarioControlador import UsuarioControlador
from tkinter import filedialog


def registrarse():
    usuario_controlador = UsuarioControlador()

    root = tk.Tk()
    root.title("Registrarse")

    nombre = tk.Label(root, text="Nombre")
    nombre.pack()
    nombre_entrada = tk.Entry(root)
    nombre_entrada.pack()

    apellido = tk.Label(root, text="Apellido")
    apellido.pack()
    apellido_entrada = tk.Entry(root)
    apellido_entrada.pack()

    email = tk.Label(root, text="Ingrese su email")
    email.pack()
    email_entrada = tk.Entry(root)
    email_entrada.pack()

    telefono = tk.Label(root, text="Ingrese su telefono")
    telefono.pack()
    telefono_entrada = tk.Entry(root)
    telefono_entrada.pack()
    
    usuario = tk.Label(root, text="Ingrese su usuario")
    usuario.pack()
    usuario_entrada = tk.Entry(root)
    usuario_entrada.pack()

    contrasena_label = tk.Label(root, text="Ingrese su contraseña")
    contrasena_label.pack()
    contrasena_entrada = tk.Entry(root, show="*")
    contrasena_entrada.pack()



    foto = tk.Label(root, text="Ingrese su foto de perfil")
    foto.pack()

    foto_blob = None  # Aca voy a almacenar la imagen

    def seleccionar_imagen():
        nonlocal foto_blob

        #guardamos en ruta_imagen la ruta de la imagen seleccionada
        ruta_imagen = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if ruta_imagen:
            with open(ruta_imagen, 'rb') as archivo_imagen: #Leemos ruta_imagen como rb (lectura binaria)
                foto_blob = archivo_imagen.read()  # Paso la imagen de rb a Blob

    boton_seleccionar_imagen = tk.Button(root, text="Seleccionar Imagen", command=seleccionar_imagen)
    boton_seleccionar_imagen.pack()


    biografia = tk.Label(root, text="Ingrese su biografia")
    biografia.pack()
    biografia_entrada = tk.Entry(root)
    biografia_entrada.pack()


    mensaje_error = None

    def evento_boton_registrarse():
        nonlocal mensaje_error
        respuesta = usuario_controlador.registrarse(nombre_entrada.get(),apellido_entrada.get(),email_entrada.get(), telefono_entrada.get() , usuario_entrada.get(), contrasena_entrada.get(), foto_blob, biografia_entrada.get())

        if not respuesta and mensaje_error is None:
            mensaje_error = tk.Label(root, text="No se pudo crear el usuario.", fg="red")
            mensaje_error.pack()

    def evento_boton_atras():
        from vista.inicio_sesion import iniciar_sesion
        root.destroy()
        iniciar_sesion()
        

    boton_atras = tk.Button(root, text="Atras", command=evento_boton_atras)
    boton_atras.pack()
    boton_registrarse = tk.Button(root, text="Registrarse", command=evento_boton_registrarse)
    boton_registrarse.pack()

    root.mainloop()
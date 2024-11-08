import tkinter as tk
from controlador.contenidoControlador import ContenidoControlador
from tkinter import filedialog
from datetime import datetime

def subir_contenido():
    contenido_controlador = ContenidoControlador()

    root = tk.Tk()
    root.title("ArtMingle - Subir Contenido")
    root.geometry("900x900")  # Tamaño de la ventana
    root.config(bg="#f8f8f8")  # Fondo claro para un diseño moderno

    title_label = tk.Label(root, text="Sube tu contenido en ArtMingle", font=("Brush Script MT", 24, "bold"), bg="#f8f8f8", fg="#ff6347")
    title_label.pack(pady=20)

    # Campos para el título y descripción
    titulo_label = tk.Label(root, text="Título", font=("Comic Sans MS", 14), bg="#f8f8f8", fg="#333")
    titulo_label.pack()
    titulo_entrada = tk.Entry(root, font=("Comic Sans MS", 12), width=30, bd=2, relief="solid", bg="#fff", fg="#333")
    titulo_entrada.pack(pady=5)

    descripcion_label = tk.Label(root, text="Descripción", font=("Comic Sans MS", 14), bg="#f8f8f8", fg="#333")
    descripcion_label.pack()
    descripcion_entrada = tk.Entry(root, font=("Comic Sans MS", 12), width=30, bd=2, relief="solid", bg="#fff", fg="#333")
    descripcion_entrada.pack(pady=5)

    # Campo para cargar una imagen o video
    archivo_label = tk.Label(root, text="Carga una imagen o video", font=("Comic Sans MS", 14), bg="#f8f8f8", fg="#333")
    archivo_label.pack(pady=10)

    archivo_blob = None
    archivo_tipo = None

    def seleccionar_archivo():
        nonlocal archivo_blob, archivo_tipo
        ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png"), ("Archivos de video", "*.mp4 *.avi *.mov")])
        if ruta_archivo:
            with open(ruta_archivo, 'rb') as archivo:
                archivo_blob = archivo.read()
            archivo_tipo = "video" if ruta_archivo.lower().endswith((".mp4", ".avi", ".mov")) else "imagen"

    boton_seleccionar_archivo = tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo, font=("Comic Sans MS", 12), bg="#4CAF50", fg="white", width=20, height=2, bd=0, relief="solid", activebackground="#2ecc71")
    boton_seleccionar_archivo.pack(pady=10)

    # Variables de entrada para likes y comentarios
    likes_label = tk.Label(root, text="Likes iniciales", font=("Comic Sans MS", 14), bg="#f8f8f8", fg="#333")
    likes_label.pack()
    likes_entrada = tk.Entry(root, font=("Comic Sans MS", 12), width=30, bd=2, relief="solid", bg="#fff", fg="#333")
    likes_entrada.insert(0, "0")  # Likes iniciales en 0
    likes_entrada.pack(pady=5)

    comentarios_label = tk.Label(root, text="Comentarios iniciales", font=("Comic Sans MS", 14), bg="#f8f8f8", fg="#333")
    comentarios_label.pack()
    comentarios_entrada = tk.Entry(root, font=("Comic Sans MS", 12), width=30, bd=2, relief="solid", bg="#fff", fg="#333")
    comentarios_entrada.insert(0, "0")  # Comentarios iniciales en 0
    comentarios_entrada.pack(pady=5)

    mensaje_error = None
    def evento_boton_subir():
        nonlocal mensaje_error

        if not titulo_entrada.get() or not descripcion_entrada.get() or not archivo_blob:
            if mensaje_error:
                mensaje_error.destroy()
            mensaje_error = tk.Label(root, text="Todos los campos son obligatorios.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 12, "italic"))
            mensaje_error.pack(pady=5)
            return

        fecha_carga = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        titulo = titulo_entrada.get()
        descripcion = descripcion_entrada.get()
        likes = int(likes_entrada.get())
        comentarios = int(comentarios_entrada.get())
        url_video = archivo_blob if archivo_tipo == "video" else None
        url_imagen = archivo_blob if archivo_tipo == "imagen" else None
        id_usuario = 1  # Suponiendo que ya tienes un id de usuario

        respuesta = contenido_controlador.insertar_contenido(titulo, descripcion, fecha_carga, likes, comentarios, url_video, url_imagen, id_usuario)

        if respuesta:
            mensaje_error = tk.Label(root, text="Contenido subido correctamente.", fg="green", bg="#f8f8f8", font=("Comic Sans MS", 12, "italic"))
        else:
            mensaje_error = tk.Label(root, text="No se pudo subir el contenido.", fg="red", bg="#f8f8f8", font=("Comic Sans MS", 12, "italic"))
        mensaje_error.pack(pady=5)

    boton_subir = tk.Button(root, text="Subir Contenido", command=evento_boton_subir, font=("Comic Sans MS", 12), bg="#ff6347", fg="white", width=20, height=2, bd=0, relief="solid", activebackground="#e74c3c")
    boton_subir.pack(pady=15)

    def evento_boton_atras():
        from vista.inicio_sesion import iniciar_sesion
        root.destroy()
        iniciar_sesion()

    boton_atras = tk.Button(root, text="Atrás", command=evento_boton_atras, font=("Comic Sans MS", 12), bg="#4CAF50", fg="white", width=20, height=2, bd=0, relief="solid", activebackground="#2ecc71")
    boton_atras.pack(pady=5)

    root.mainloop()

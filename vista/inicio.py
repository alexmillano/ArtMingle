import tkinter as tk
from controlador.contenidoControlador import ContenidoControlador
from PIL import Image, ImageTk  # Necesario para mostrar imágenes

def inicio(conexion):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("ArtMingle - Vista de Inicio")
    root.geometry("900x900")
    root.config(bg="#f8f8f8")

    # Crear instancia del controlador de contenido
    contenido_controlador = ContenidoControlador(conexion)

    # Obtener contenidos de la base de datos
    contenidos = contenido_controlador.obtener_contenidos()

    # Botón para subir contenido
    def ir_a_subir_contenido():
        root.destroy()
        from vista.subir_contenido import subir_contenido  # Importar la función para subir contenido
        subir_contenido()

    boton_subir_contenido = tk.Button(
        root, text="Subir Contenido", command=ir_a_subir_contenido,
        font=("Comic Sans MS", 12), bg="#4CAF50", fg="white",
        width=15, height=2, bd=0, relief="solid", activebackground="#2ecc71"
    )
    boton_subir_contenido.pack(anchor="ne", padx=20, pady=10)  # Colocar el botón en la esquina superior derecha

    # Contenedor para las publicaciones
    contenedor_contenidos = tk.Frame(root, bg="#f8f8f8")
    contenedor_contenidos.pack(fill="both", expand=True)

    # Crear una entrada de contenido para cada publicación
    for contenido in contenidos:
        # Obtener los datos de cada contenido
        id_usuario = contenido[7]  # Suponiendo que idUsuario está en la posición 7
        titulo = contenido[1]
        descripcion = contenido[2]
        fecha_carga = contenido[3]
        url_imagen = contenido[6]  # Suponiendo que urlImagen está en la columna 6

        # Crear un marco para cada contenido
        marco_contenido = tk.Frame(contenedor_contenidos, bg="#ffffff", bd=2, relief="solid")
        marco_contenido.pack(pady=10, padx=20, fill="x")

        # Mostrar el nombre del usuario (suponiendo que tienes una forma de obtenerlo)
        nombre_usuario_label = tk.Label(
            marco_contenido, text=f"Usuario {id_usuario}",
            font=("Comic Sans MS", 14, "bold"), bg="#ffffff", fg="#333"
        )
        nombre_usuario_label.pack(anchor="w", padx=10, pady=(10, 5))

        # Mostrar el título del contenido
        titulo_label = tk.Label(
            marco_contenido, text=titulo,
            font=("Comic Sans MS", 12, "italic"), bg="#ffffff", fg="#666"
        )
        titulo_label.pack(anchor="w", padx=10)

        # Mostrar la descripción del contenido
        descripcion_label = tk.Label(
            marco_contenido, text=descripcion,
            font=("Comic Sans MS", 12), bg="#ffffff", fg="#333"
        )
        descripcion_label.pack(anchor="w", padx=10, pady=(5, 10))

        # Cargar y mostrar la imagen (si existe)
        if url_imagen:
            try:
                imagen = Image.open(url_imagen)
                imagen = imagen.resize((200, 200))  # Redimensionar la imagen
                imagen_tk = ImageTk.PhotoImage(imagen)
                imagen_label = tk.Label(marco_contenido, image=imagen_tk, bg="#ffffff")
                imagen_label.image = imagen_tk  # Mantener referencia para evitar que se elimine
                imagen_label.pack(anchor="center", padx=10, pady=(5, 10))
            except Exception as e:
                print(f"No se pudo cargar la imagen: {e}")

        # Fecha de publicación
        fecha_label = tk.Label(
            marco_contenido, text=f"Publicado el: {fecha_carga}",
            font=("Comic Sans MS", 10), bg="#ffffff", fg="#888"
        )
        fecha_label.pack(anchor="w", padx=10, pady=(0, 10))

    root.mainloop()

import tkinter as tk

def paginainicio():
    root = tk.Tk()
    root.title("ArtMingle - Vista de Inicio")
    root.geometry("900x900")  
    root.config(bg="#f8f8f8")  

    saludo_label = tk.Label(root, text="¡Bienvenido a ArtMingle!", font=("Brush Script MT", 32, "bold"), bg="#f8f8f8", fg="#ff6347")
    saludo_label.pack(pady=40)


    usuario_label = tk.Label(root, text=f"Hola, Artista!", font=("Comic Sans MS", 20), bg="#f8f8f8", fg="#333")
    usuario_label.pack(pady=20)

    descripcion_label = tk.Label(root, text="¡Bienvenido a la plataforma social para artistas! Conéctate, comparte tu arte, y más.", font=("Comic Sans MS", 16), bg="#f8f8f8", fg="#333")
    descripcion_label.pack(pady=20)

    root.mainloop()
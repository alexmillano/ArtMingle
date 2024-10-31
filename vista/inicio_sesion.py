import tkinter as tk;

root = tk.Tk()
root.title=("Iniciar sesion")

email= tk.Label(root,text="Ingrese su email")
email.pack()
email_entrada=tk.Entry(root)
email_entrada.pack()


contrasena= tk.Label(root,text="Ingrese su contraseña")
contrasena.pack()
contrasena_entrada=tk.Entry(root)
contrasena_entrada.pack()

boton=tk.Button(root, text="Ingresar" )
boton.pack()


root.mainloop()
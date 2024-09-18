import tkinter as tk  
from tkinter import messagebox, Menu

class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

class GestorRecetas:      
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

def agregar_receta():
    nombre = entry_nombre.get()
    ingredientes = entry_ingredientes.get().split(",") 
    ingredientes = [ing.strip() for ing in ingredientes if ing.strip()]  # Remove empty entries

    if nombre and ingredientes:
        gestor.agregar_receta(nombre, ingredientes)
        listbox_recetas.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")

def ver_ingredientes():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]
        ingredientes = ", ".join(receta.ingredientes)
        messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"{ingredientes}")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")

def eliminar_receta():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_receta(indice)
        if nombre:
            listbox_recetas.delete(indice)
            messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la receta.")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para eliminar.")

def salir():
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
        ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Recetas")

gestor = GestorRecetas()

# Menú
menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)

# Menú "Archivo"
menu_archivo = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=salir)

# Etiquetas y entradas para el nombre y los ingredientes
label_nombre = tk.Label(ventana, text="Nombre de la receta:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

label_ingredientes = tk.Label(ventana, text="Ingredientes (separados por coma):")
label_ingredientes.pack(pady=5)
entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack(pady=5)

# Botón para agregar receta
btn_agregar = tk.Button(ventana, text="Agregar receta", command=agregar_receta)
btn_agregar.pack(pady=10)

# Listbox para mostrar las recetas guardadas
listbox_recetas = tk.Listbox(ventana)
listbox_recetas.pack(pady=10)

# Botones para ver y eliminar recetas
btn_ver = tk.Button(ventana, text="Ver ingredientes", command=ver_ingredientes)
btn_ver.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar receta", command=eliminar_receta)
btn_eliminar.pack(pady=5)

btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.pack()


# Iniciar el bucle principal de la ventana
ventana.mainloop()

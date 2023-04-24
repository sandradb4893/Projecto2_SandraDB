import json
from tkinter import messagebox

# Patrón de diseño Singleton para manejar la lista de estudiantes
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
# Clase para representar a un estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

# Clase Factory para crear estudiantes
class EstudianteFactory:
    def crear_estudiante(self, nombre, edad, grado):
        return Estudiante(nombre, edad, grado)

# Clase para manejar la lista de estudiantes
class EstudianteList(metaclass=Singleton):
    def __init__(self):
        self.estudiantes = []
        self.estudiante_factory = EstudianteFactory()

    def agregar_estudiante(self, nombre, edad, grado):
        estudiante = self.estudiante_factory.crear_estudiante(nombre, edad, grado)
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None

    def eliminar_estudiante(self, nombre):
        estudiante = self.buscar_estudiante(nombre)
        if estudiante:
            self.estudiantes.remove(estudiante)

    def get_estudiante_nombres(self):
        return [estudiante.nombre for estudiante in self.estudiantes]

    def get_estudiante_edades(self):
        return [estudiante.edad for estudiante in self.estudiantes]

    def get_estudiante_grados(self):
        return [estudiante.grado for estudiante in self.estudiantes]

    def to_dict_list(self):
        return [{
            "Nombre": estudiante.nombre,
            "Edad": estudiante.edad,
            "Grado": estudiante.grado,
        } for estudiante in self.estudiantes]

# Función para agregar un estudiante al sistema
def agregar_estudiante(nombre, edad, grado):
    try:
        estudiante_list = EstudianteList()
        estudiante_list.agregar_estudiante(nombre, edad, grado)
        messagebox.showinfo("Éxito", f"El estudiante {nombre} se agregó al sistema")
    except:
        messagebox.showerror("Error no se pudo agregar el estudiante al sistema")


# Función para buscar un estudiante en el sistema
def buscar_estudiante(nombre):
    try:
        estudiante_list = EstudianteList()
        estudiante = estudiante_list.buscar_estudiante(nombre)
        if estudiante:
            messagebox.showinfo("Resultado", f"Nombre: {estudiante.nombre}\nEdad: {estudiante.edad}\nGrado: {estudiante.grado}\n")
        else:
            messagebox.showerror("Error", f"No se encontró ningún estudiante con el nombre {nombre}")
    except:
        messagebox.showerror("Error no se encontró al estudiante en el sistema")

# Función para mostrar la lista completa de estudiantes en el sistema
def mostrar_estudiante_list():
    try:
        estudiante_list = EstudianteList()
        estudiante_nombres = estudiante_list.get_estudiante_nombres()
        if estudiante_nombres:
            estudiante_list_str = "\n".join(estudiante_nombres)
            messagebox.showinfo("Lista de estudiantes", estudiante_list_str)
        else:
            messagebox.showwarning("Advertencia", "No hay estudiantes en el sistema")
    except:
        messagebox.showerror("Error no se puede mostrar al estudiante")
# Función para eliminar un estudiante del sistema
def eliminar_estudiante(nombre):
    try:
        estudiante_list = EstudianteList()
        estudiante_list.eliminar_estudiante(nombre)
        messagebox.showinfo("Éxito", f"El estudiante {nombre} se eliminó del sistema")
    except:
        messagebox.showerror("Error no se eliminó al estudiante del sistema")


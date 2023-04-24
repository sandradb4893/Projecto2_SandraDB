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


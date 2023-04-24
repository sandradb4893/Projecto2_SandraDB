from tkinter import messagebox

import Funciones
# Función para manejar la opción seleccionada en el menú
def menu_opcion(opcion, nombre_entry, edad_entry, grado_entry, filename_entry):
    try:
        if opcion == 1:
            nombre = nombre_entry.get()
            edad = int(edad_entry.get())
            grado = int(grado_entry.get())
            Funciones.agregar_estudiante(nombre, edad, grado)
        elif opcion == 2:
            nombre = nombre_entry.get()
            Funciones.buscar_estudiante(nombre)
        elif opcion == 3:
            Funciones.mostrar_estudiante_list()
        elif opcion == 4:
            nombre = nombre_entry.get()
            Funciones.eliminar_estudiante(nombre)
        elif opcion == 5:
            filenombre = filename_entry.get()
            Funciones.guardar_estudiante_list(filenombre)
        elif opcion == 6:
            filenombre = filename_entry.get()
            Funciones.cargar_estudiante_list(filenombre)
    except:
        messagebox.showerror("Error en el sistema")

# Crear menú
menu = tk.Menu(root)
root.config(menu=menu)

# Crear opciones del menú
file_menu = tk.Menu(menu)
menu.add_cascade(label="Sistema para registro de estudiantes", menu=file_menu)
file_menu.add_command(label="Agregar estudiante", command=lambda: MenuOpciones.menu_opcion(1, nombre_entry, edad_entry, grado_entry,filename_entry))
file_menu.add_command(label="Buscar estudiante", command=lambda: MenuOpciones.menu_opcion(2, nombre_entry, edad_entry, grado_entry, filename_entry))
file_menu.add_command(label="Mostrar lista completa", command=lambda: MenuOpciones.menu_opcion(3, nombre_entry, edad_entry, grado_entry, filename_entry))
file_menu.add_command(label="Eliminar estudiante", command=lambda: MenuOpciones.menu_opcion(4, nombre_entry, edad_entry, grado_entry, filename_entry))
file_menu.add_command(label="Guardar lista de estudiantes", command=lambda: MenuOpciones.menu_opcion(5, nombre_entry, edad_entry, grado_entry, filename_entry))
file_menu.add_command(label="Cargar lista de estudiantes", command=lambda: MenuOpciones.menu_opcion(6, nombre_entry, edad_entry, grado_entry, filename_entry))

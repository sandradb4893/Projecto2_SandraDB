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
# Crear botones para realizar acciones
agregar_button = Button(root, text="Agregar estudiante", command=lambda: MenuOpciones.menu_opcion(1, nombre_entry, edad_entry, grado_entry,filename_entry))
agregar_button.grid(row=4, column=0, padx=5, pady=5)

buscar_button = Button(root, text="Buscar estudiante", command=lambda: MenuOpciones.menu_opcion(2, nombre_entry, edad_entry, grado_entry, filename_entry))
buscar_button.grid(row=5, column=0, padx=5, pady= 5)

mostrar_button = Button(root, text="Mostrar lista completa", command=lambda: MenuOpciones.menu_opcion(3, nombre_entry, edad_entry, grado_entry, filename_entry))
mostrar_button.grid(row=6, column=0, padx=5, pady=5)

eliminar_button = Button(root, text="Eliminar estudiante", command=lambda: MenuOpciones.menu_opcion(4, nombre_entry, edad_entry, grado_entry, filename_entry))
eliminar_button.grid(row=7, column=0, padx=5, pady=5)

file_menu.add_command(label="Guardar lista de estudiantes", command=lambda: MenuOpciones.menu_opcion(5, nombre_entry, edad_entry, grado_entry, filename_entry))
file_menu.add_command(label="Cargar lista de estudiantes", command=lambda: MenuOpciones.menu_opcion(6, nombre_entry, edad_entry, grado_entry, filename_entry))

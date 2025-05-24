"""
Sistema de Gestión de Pasajes Aéreos - SkyRoute S.R.L.
Versión prototipo (Evidencia de Aprendizaje 2)
Para instalar el sistema, se debe tener Python. Para ejecutar la aplicación, usa el siguiente comando en la terminal: main.py. 
Seguí las instrucciones en pantalla para navegar por el menú. 
Este prototipo simula el sistema de gestión de pasajes de SkyRoute S.R.L., permitiéndote gestionar clientes, destinos y ventas.
Integrantes del grupo:
- Amaya, Paula. DNI: 40.403.171
- Martinez, Cristian. DNI: 31.819.114
-
-
-
-
-
"""

print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")

salir = False
while not salir:
    print("\nMenú Principal:")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Registrar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver lista de clientes")
        print("2. Agregar nuevo cliente")
        print("3. Modificar datos de un cliente")
        print("4. Eliminar Cliente")
        print("5. Buscar clientes")
        print("6. Volver al menú principal")
        subopcion = input("Seleccione una opción: ")
        if subopcion == "1":
            print("Eligió: Ver lista de clientes")
        elif subopcion == "2":
            print("Eligió: Agregar nuevo cliente")
            print("Ingrese datos del nuevo cliente ...")
        elif subopcion == "3":
            print("Eligió: Modificar datos de un cliente")
        elif subopcion == "4":
            print("Eligió: Eliminar Cliente")
        elif subopcion == "5":
            print("Eligió: Buscar clientes")
            print("Ingrese DNI/CUILT del cliente ...")
        elif subopcion == "6":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida")

    elif opcion == "2":
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Buscar destino")
        print("2. Agregar nuevo destino")
        print("3. Emilinar destino")
        print("4. Volver al menú principal")
        subopcion = input("Seleccione una opción: ")
        if subopcion == "1":
            print("Eligió: Buscar destino")
            print("Ingrese destino ...")
        elif subopcion == "2":
            print("Eligió: Agregar nuevo destino")
            print("Ingrese datos del nuevo destino ...")
        elif subopcion == "3":
            print("Eligió: Emilinar destino")
            print("Seleccione destino para eliminar ...")                 
        elif subopcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida")

    elif opcion == "3":
        print("\n -- REGISTRAR VENTAS -- ")
        print("Ingrese cliente ...")
        print("Ingrese destino ...")
        print("Ingrese fecha ...")
        print("Ingrese costo ...")

    elif opcion == "4":
        print("\n-- CONSULTAR VENTAS --")
        print("1. Ver todas las ventas")
        print("2. Ventas por cliente")
        print("3. Ventas por periodo")
        print("4. Ventas por destino")
        print("5. Ventas por estado (Activa/Anulada)")
        print("5. Volver al Menú Principal")
        subopcion = input("Seleccione una opción: ")
        if subopcion == "1":
            print("Eligió: Ver todas las ventas")
        elif subopcion == "2":
            print("Eligió: Ventas por cliente")
        elif subopcion == "3":
            print("Eligió: Ventas por periodo")
        elif subopcion == "4":
            print("Eligió: Ventas por destino")
        elif subopcion == "5":
            print("Eligió: Ventas por estado (Activa/Anulada)")
        elif subopcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida")

    elif opcion == "5":
        print("\n -- BOTON DE ARREPENTIEMIENTO -- ")

    elif opcion == "6":
        print("Saliendo del sistema. ¡Gracias por usar SkyRoute!")
        salir = True

    else:
        print("Opción no válida. Intente nuevamente.")
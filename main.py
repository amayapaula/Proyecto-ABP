"""
SkyRoute S.R.L. - Sistema de Gestión de Pasajes
Versión Prototipo - Evidencia de Aprendizaje 2 

Propósito del sistema
Este sistema fue desarrollado para simular el funcionamiento de una aplicación de gestión de pasajes aéreos para la empresa SkyRoute S.R.L. 
Su objetivo es organizar y facilitar el registro de clientes, destinos disponibles y operaciones de venta de pasajes. Además, incorpora una funcionalidad de "Botón de Arrepentimiento"
que permite simular la anulación de una venta reciente.

Instalción 
- Tener instalado Python.
- Descargá o cloná la carpeta del proyecto que contiene el archivo `main.py`.
- Abrí una terminal en la carpeta del archivo.
- Ejecutá el comando: python main.py
- Seguí las instrucciones en pantalla para navegar por el menú del sistema.

Integrantes del grupo
- Amaya, Paula. DNI: 40.403.171
- Martinez, Cristian. DNI: 31.819.114
- Guillermo, Bianco DNI: 35.669.345
- Alfonsina, Abrego DNI: 30.971.691
- Valeria, Cortez DNI: 29.768.588
"""

print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")

salir = False
while not salir:
    print("\n-- MENÚ PRINCIPAL: --")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Registrar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            print("\n-- GESTIONAR CLIENTES --")
            print("1. Ver lista de clientes")
            print("2. Agregar nuevo cliente")
            print("3. Agregar nueva empresa")
            print("4. Modificar cliente")
            print("5. Eliminar cliente")
            print("6. Buscar clientes")
            print("7. Volver al menú principal")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                print("Lista de clientes")
            elif subopcion == "2":
                print("Agregar nuevo cliente")
                print("Ingrese DNI de cliente: ...") ## Luego se desarrollarán las funciones para almacenar datos
                print("Ingrese correo electrónico: ... ")
                print("Ingrese fecha de nacimiento: ...")
            elif subopcion == "3":
                print("Agregar nueva empresa")
                print ("Ingrese CUIL de empresa: ...")   
            elif subopcion == "4":
                print("Modificar cliente")
            elif subopcion == "5":
                print("Eliminar cliente")
            elif subopcion == "6":
                print("Buscar clientes")
                print("Ingrese DNI de cliente: ...")
            elif subopcion == "7":
                print("Volviendo al menú principal")
                break
            else:
                print("Opción no válida")

    elif opcion == "2":
        while True:
            print("\n-- GESTIONAR DESTINOS --")
            print("1. Buscar destino")
            print("2. Agregar nuevo destino")
            print("3. Eliminar destino")
            print("4. Volver al menú principal")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                print("Buscar destino")
                print("Ingrese destino: ...")
            elif subopcion == "2":
                print("Agregar nuevo destino")
                print("Ingrese datos del nuevo destino: ...")
            elif subopcion == "3":
                print("Eliminar destino")
                print("Ingrese destino para eliminar: ")                 
            elif subopcion == "4":
                print("Volviendo al menú principal")
                break
            else:
                print("Opción no válida")

    elif opcion == "3":        
        while True:
            print("\n -- REGISTRAR VENTAS -- ")
            print("1. Ingrese cliente")
            print("2. ¿Es empresa?")
            print("3. Ingrese destino ")
            print("4. Ingrese vuelo")
            print("5. Ingrese clase")
            print("6. Ingrese fecha")
            print("7. Ingrese costo")
            print("8. Volver al menú principal")
            subopcion = input ("Seleccione una opción: ")
            if subopcion == "1":
                print("Cliente")
                print("Ingrese DNI de cliente: ...")
                print("Ingrese correo electrónico de cliente: ...")            
            elif subopcion == "2":
                print("Empresa")
                print("Ingrese CUIL de empresa: ...")
            elif subopcion == "3":
                print("Destino")
                print("Ingrese destino: ...")
            elif subopcion == "4":
                print("Vuelo")
                print("Ingrese si es Ida / Ida y vuelta: ...")
            elif subopcion == "5":
                print("Clase")
                print("Ingrese Económica / Business / Primera Clase: ...")
            elif subopcion == "6":
                print("Fecha de vuelo")
                print("Ingrese fecha de vuelo: ...")
                print("Ingrese fecha de venta: ...") ## Preguntar si se puede capturar la fecha directamente sin que se ingrese
            elif subopcion == "7":
                print("Costo de pasajes")
                print("Ingrese costo total: ...")            
            elif subopcion == "8":
                print("Volviendo al menú principal")
                break
            else:
                print("Opción no válida")

    elif opcion == "4":
        while True:
            print("\n-- CONSULTAR VENTAS --")
            print("1. Ver todas las ventas")
            print("2. Ventas por cliente")
            print("3. Ventas por periodo")
            print("4. Ventas por destino")
            print("5. Ventas por estado (Activa / Anulada)")
            print("5. Volver al menú principal")
            subopcion = input("Seleccione una opción: ")
            if subopcion == "1":
                print("Ver todas las ventas")
            elif subopcion == "2":
                print("Ventas por cliente")
            elif subopcion == "3":
                print("Ventas por periodo")
            elif subopcion == "4":
                print("Ventas por destino")
            elif subopcion == "5":
                print("Ventas por estado (Activa / Anulada)")
            elif subopcion == "5":
                print("Volviendo al menú principal")
                break
            else:
                print("Opción no válida")

    elif opcion == "5":
        print("\n -- BOTON DE ARREPENTIEMIENTO -- ")

    elif opcion == "6":
        print("Saliendo del sistema. ¡Gracias por usar SkyRoute!")
        salir = True

    else:
        print("Opción no válida. Intente nuevamente.")



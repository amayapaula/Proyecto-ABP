"""
SkyRoute S.R.L. - Sistema de Gestión de Pasajes
Versión Prototipo - Evidencia de Aprendizaje 3

Propósito del sistema
Este sistema fue desarrollado para simular el funcionamiento de una aplicación de gestión de pasajes aéreos para la empresa SkyRoute S.R.L. 
Su objetivo es organizar y facilitar el registro de clientes, destinos disponibles y operaciones de venta de pasajes. Además, incorpora una funcionalidad de "Botón de Arrepentimiento"
que permite simular la anulación de una venta reciente.

Instalación 
- Tener instalado Python.
- Descargá o cloná la carpeta del proyecto que contiene el archivo `main.py`.
- Abrí una terminal en la carpeta del archivo.
- Ejecutá el comando: python main.py
- Seguí las instrucciones en pantalla para navegar por el menú del sistema.

Integrantes del grupo
- Amaya, Paula. DNI: 40.403.171
- Martinez, Cristian. DNI: 31.819.114
- Guillermo, Bianco DNI: 35.669.345
- Valeria, Cortez DNI: 29.768.588
"""

from clientes import (
    ver_clientes,
    agregar_cliente,
    modificar_cliente,
    eliminar_cliente,
    buscar_cliente_por_dni
)

from destinos import gestionar_destinos, listar_destinos
from ventas import registrar_venta, consultar_ventas
from arrepentimiento import boton_arrepentimiento

# Menú principal del sistema
def menu_principal():
    print("\n-- MENÚ PRINCIPAL: --")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Registrar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Salir")
    return input("Seleccione una opción: ")

# Menú de gestión de clientes
def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver lista de clientes")
        print("2. Agregar nuevo cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Buscar clientes")
        print("6. Volver al menú principal")
        subopcion = input("Seleccione una opción: ")
        if subopcion == "1":
            ver_clientes()
        elif subopcion == "2":
            agregar_cliente()
        elif subopcion == "3":
            modificar_cliente()
        elif subopcion == "4":
            eliminar_cliente()
        elif subopcion == "5":
            buscar_cliente_por_dni()
        elif subopcion == "6":
            break
        else:
            print("Opción no válida.")

# Registro de una nueva venta
def gestionar_venta():
    print("\n-- REGISTRAR VENTA --")
    print("Clientes disponibles:")
    ver_clientes()
    id_cliente = input("Ingrese el ID del cliente: ").strip()
    if not id_cliente.isdigit():
        print("ID de cliente no válido.")
        return

    print("\nDestinos disponibles:")
    listar_destinos()
    id_destino = input("Ingrese el ID del destino: ").strip()
    if not id_destino.isdigit():
        print("ID de destino no válido.")
        return

    costo_total = input("Ingrese el costo total: ").strip()
    try:
        costo_total = float(costo_total)
    except ValueError:
        print("Costo total inválido.")
        return

    registrar_venta(int(id_cliente), int(id_destino), costo_total)

# Punto de entrada principal del sistema
def main():
    print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    salir = False
    while not salir:
        opcion = menu_principal()

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_destinos()
        elif opcion == "3":
            gestionar_venta()
        elif opcion == "4":
            consultar_ventas()
        elif opcion == "5":
            boton_arrepentimiento()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Gracias por usar SkyRoute!")
            salir = True
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

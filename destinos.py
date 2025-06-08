import mysql.connector
from conexion import conectar

# Agrega un nuevo destino a la base de datos
def agregar_destino(ciudad, pais, costo_base):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO destino (ciudad, pais, costo_base)
            VALUES (%s, %s, %s)
        """
        cursor.execute(consulta, (ciudad, pais, costo_base))
        conexion.commit()
        print("Destino agregado exitosamente.")
    except mysql.connector.Error as e:
        print("Error al agregar destino:", e)
    finally:
        cursor.close()
        conexion.close()

# Lista todos los destinos registrados
def listar_destinos():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destino")
        destinos = cursor.fetchall()
        if destinos:
            print("\n-- Destinos disponibles --")
            for d in destinos:
                print(f"ID: {d['id_destino']} | Ciudad: {d['ciudad']} | País: {d['pais']} | Costo base: {d['costo_base']}")
        else:
            print("No hay destinos registrados.")
    except mysql.connector.Error as e:
        print("Error al listar destinos:", e)
    finally:
        cursor.close()
        conexion.close()

# Menú para gestionar destinos
def gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver destinos disponibles")
        print("2. Agregar nuevo destino")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_destinos()
        elif opcion == "2":
            ciudad = input("Ingrese ciudad: ").strip()
            pais = input("Ingrese país: ").strip()
            try:
                costo_base = float(input("Ingrese costo base: ").strip())
                agregar_destino(ciudad, pais, costo_base)
            except ValueError:
                print("El costo base debe ser un número válido.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

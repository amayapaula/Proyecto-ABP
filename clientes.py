from conexion import conectar
import mysql.connector

# Muestra todos los clientes registrados
def ver_clientes():
    conexion = None
    cursor = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        if clientes:
            print("\n-- Lista de Clientes --")
            for cliente in clientes:
                print(cliente)
        else:
            print("No hay clientes registrados.")
    except mysql.connector.Error as err:
        print("Error al obtener clientes:", err)
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

# Agrega un nuevo cliente (persona o agencia)
def agregar_cliente():
    razon_social = input("Ingrese razón social o nombre: ").strip()
    cuit = input("Ingrese CUIT/DNI: ").strip()
    correo_contacto = input("Ingrese correo de contacto: ").strip()
    tipo_cliente = input("Ingrese tipo de cliente (Persona/Agencia): ").strip()

    if not (razon_social and cuit and correo_contacto and tipo_cliente):
        print("Todos los campos son obligatorios.")
        return

    if tipo_cliente.lower() not in ['persona', 'agencia']:
        print("Tipo de cliente inválido. Debe ser 'Persona' o 'Agencia'.")
        return

    tipo_cliente = tipo_cliente.capitalize()

    conexion = None
    cursor = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO cliente (razon_social, cuit, correo_contacto, tipo_cliente)
            VALUES (%s, %s, %s, %s)
        """
        valores = (razon_social, cuit, correo_contacto, tipo_cliente)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Cliente agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al agregar cliente:", err)
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

# Modifica datos de un cliente existente
def modificar_cliente():
    conexion = None
    cursor = None
    try:
        id_cliente = input("Ingrese el ID del cliente a modificar: ").strip()

        if not id_cliente.isdigit():
            print("Debe ingresar un ID válido.")
            return

        nuevo_razon_social = input("Nuevo nombre o razón social (dejar vacío para mantener): ").strip()
        nuevo_cuit = input("Nuevo CUIT/DNI (dejar vacío para mantener): ").strip()
        nuevo_correo = input("Nuevo correo de contacto (dejar vacío para mantener): ").strip()
        nuevo_tipo = input("Nuevo tipo de cliente (Persona/Agencia, dejar vacío para mantener): ").strip()

        if nuevo_tipo and nuevo_tipo.lower() not in ['persona', 'agencia']:
            print("Tipo de cliente inválido. Debe ser 'Persona' o 'Agencia'.")
            return
        if nuevo_tipo:
            nuevo_tipo = nuevo_tipo.capitalize()

        conexion = conectar()
        cursor = conexion.cursor()

        if nuevo_razon_social:
            cursor.execute("UPDATE cliente SET razon_social = %s WHERE id_cliente = %s", (nuevo_razon_social, id_cliente))
        if nuevo_cuit:
            cursor.execute("UPDATE cliente SET cuit = %s WHERE id_cliente = %s", (nuevo_cuit, id_cliente))
        if nuevo_correo:
            cursor.execute("UPDATE cliente SET correo_contacto = %s WHERE id_cliente = %s", (nuevo_correo, id_cliente))
        if nuevo_tipo:
            cursor.execute("UPDATE cliente SET tipo_cliente = %s WHERE id_cliente = %s", (nuevo_tipo, id_cliente))

        conexion.commit()
        print("Cliente modificado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al modificar cliente:", err)
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

# Elimina un cliente por ID
def eliminar_cliente():
    conexion = None
    cursor = None
    try:
        id_cliente = input("Ingrese el ID del cliente a eliminar: ").strip()
        if not id_cliente.isdigit():
            print("Debe ingresar un ID válido.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        conexion.commit()
        print("Cliente eliminado correctamente.")
    except mysql.connector.Error as err:
        print("Error al eliminar cliente:", err)
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

# Busca clientes por CUIT/DNI
def buscar_cliente_por_dni():
    conexion = None
    cursor = None
    try:
        cuit = input("Ingrese el CUIT/DNI del cliente: ").strip()
        if not cuit:
            print("Debe ingresar un CUIT/DNI válido.")
            return

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente WHERE cuit = %s", (cuit,))
        cliente = cursor.fetchone()
        if cliente:
            print("Cliente encontrado:", cliente)
        else:
            print("No se encontró ningún cliente con ese CUIT/DNI.")
    except mysql.connector.Error as err:
        print("Error al buscar cliente:", err)
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

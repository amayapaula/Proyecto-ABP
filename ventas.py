# ventas.py
import mysql.connector
from conexion import conectar
from datetime import date

# Registra una nueva venta en la base de datos
def registrar_venta(id_cliente, id_destino, costo_total):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO venta (id_cliente, id_destino, fecha_venta, costo_total, estado)
            VALUES (%s, %s, %s, %s, 'Activa')
        """
        cursor.execute(consulta, (id_cliente, id_destino, date.today(), costo_total))
        conexion.commit()
        print("Venta registrada exitosamente.")
    except mysql.connector.Error as e:
        print("Error al registrar la venta:", e)
    finally:
        cursor.close()
        conexion.close()

# Consulta todas las ventas registradas
def consultar_ventas():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM venta") # Sentencia SQL
        ventas = cursor.fetchall()
        for v in ventas:
            print(v)
    except mysql.connector.Error as e:
        print("Error al consultar ventas:", e)
    finally:
        cursor.close()
        conexion.close()

# destinos.py
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
        for d in destinos:
            print(d)
    except mysql.connector.Error as e:
        print("Error al listar destinos:", e)
    finally:
        cursor.close()
        conexion.close()

# arrepentimiento.py
import mysql.connector
from conexion import conectar
from datetime import date

# Registra la anulación de una venta con motivo
def registrar_arrepentimiento(id_venta, motivo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Primero anulamos la venta
        actualizar_estado = "UPDATE venta SET estado = 'Anulada' WHERE id_venta = %s"
        cursor.execute(actualizar_estado, (id_venta,))

        # Luego registramos en la tabla arrepentimiento
        consulta = """
            INSERT INTO arrepentimiento (id_venta, fecha_anulacion, motivo)
            VALUES (%s, %s, %s)
        """
        cursor.execute(consulta, (id_venta, date.today(), motivo))
        conexion.commit()
        print("Venta anulada y arrepentimiento registrado.")
    except mysql.connector.Error as e:
        print("Error al registrar arrepentimiento:", e)
    finally:
        cursor.close()
        conexion.close()

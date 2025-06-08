import mysql.connector
from conexion import conectar
from datetime import date

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

def consultar_ventas():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        consulta = """
            SELECT v.id_venta, c.razon_social AS cliente, d.ciudad AS destino, v.fecha_venta, v.costo_total, v.estado
            FROM venta v
            JOIN cliente c ON v.id_cliente = c.id_cliente
            JOIN destino d ON v.id_destino = d.id_destino
            ORDER BY v.fecha_venta DESC
        """
        cursor.execute(consulta)
        ventas = cursor.fetchall()
        if not ventas:
            print("No hay ventas registradas.")
            return
        print("\n-- Lista de Ventas --")
        for v in ventas:
            print(f"ID Venta: {v['id_venta']}, Cliente: {v['cliente']}, Destino: {v['destino']}, "
                  f"Fecha: {v['fecha_venta']}, Costo: ${v['costo_total']}, Estado: {v['estado']}")
    except mysql.connector.Error as e:
        print("Error al consultar ventas:", e)
    finally:
        cursor.close()
        conexion.close()

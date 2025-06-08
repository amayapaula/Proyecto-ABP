
import mysql.connector
from conexion import conectar
from datetime import date, datetime, timedelta

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

# Opción del menú para ejecutar el botón de arrepentimiento
def boton_arrepentimiento():
    try:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        # Mostrar ventas activas
        cursor.execute("SELECT * FROM venta WHERE estado = 'Activa'")
        ventas_activas = cursor.fetchall()
        
        if not ventas_activas:
            print("No hay ventas activas para anular.")
            return

        print("\n-- Ventas activas --")
        for v in ventas_activas:
            print(f"ID Venta: {v['id_venta']} | Cliente: {v['id_cliente']} | Destino: {v['id_destino']} | Fecha: {v['fecha_venta']} | Costo: {v['costo_total']}")

        id_venta = input("Ingrese el ID de la venta que desea anular: ").strip()
        if not id_venta.isdigit():
            print("ID inválido.")
            return

        # Obtener la venta específica
        cursor.execute("SELECT * FROM venta WHERE id_venta = %s AND estado = 'Activa'", (id_venta,))
        venta = cursor.fetchone()

        if not venta:
            print("Venta no encontrada o ya fue anulada.")
            return

        # ----- Validación original de 60 días -----
        # """
        # fecha_venta = venta['fecha_venta']
        # if (date.today() - fecha_venta).days > 60:
        #     print("No se puede anular la venta. Han pasado más de 60 días desde la compra.")
        #     return
        # """

        # ----- Validación temporal para pruebas (60 segundos) -----
        fecha_venta = venta['fecha_venta']
        fecha_actual = datetime.now()

        # Convertir fecha_venta a datetime si solo es date
        if isinstance(fecha_venta, date):
            fecha_venta = datetime.combine(fecha_venta, datetime.min.time())

        if (fecha_actual - fecha_venta).total_seconds() > 60:
            print("No se puede anular la venta. Han pasado más de 60 segundos desde la compra (modo prueba).")
            return

        motivo = input("Ingrese el motivo de la anulación: ").strip()
        registrar_arrepentimiento(id_venta, motivo)

    except mysql.connector.Error as e:
        print("Error en el botón de arrepentimiento:", e)
    finally:
        cursor.close()
        conexion.close()

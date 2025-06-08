from datetime import date, timedelta
import mysql.connector
from conexion import conectar

def registrar_arrepentimiento(id_venta, motivo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Obtener fecha de venta
        consulta_fecha = "SELECT fecha_venta FROM venta WHERE id_venta = %s"
        cursor.execute(consulta_fecha, (id_venta,))
        resultado = cursor.fetchone()
        if not resultado:
            print("Venta no encontrada.")
            return
        
        fecha_venta = resultado[0]
        fecha_limite = fecha_venta + timedelta(days=60)

        if date.today() > fecha_limite:
            print("No se puede anular la venta: superó el límite de 60 días desde la reserva.")
            return

        # Cambiar estado de venta a 'Anulada'
        actualizar_estado = "UPDATE venta SET estado = 'Anulada' WHERE id_venta = %s"
        cursor.execute(actualizar_estado, (id_venta,))

        # Registrar en tabla arrepentimiento
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

def boton_arrepentimiento():
    print("\n-- BOTÓN DE ARREPENTIMIENTO --")
    id_venta = input("Ingrese el ID de la venta a anular: ").strip()
    if not id_venta.isdigit():
        print("ID de venta no válido.")
        return
    motivo = input("Ingrese el motivo del arrepentimiento: ").strip()
    if not motivo:
        print("El motivo es obligatorio.")
        return
    registrar_arrepentimiento(int(id_venta), motivo)

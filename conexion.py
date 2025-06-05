import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="sky_route"
    )
    return conexion
1
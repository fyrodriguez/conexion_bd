import psycopg



def obtener_conexion():
    return psycopg.connect(
        host="192.168.1.71",
        port="5432",
        bdname="conexion",
        user="postgres",
        password="Alejandro10*"
    )
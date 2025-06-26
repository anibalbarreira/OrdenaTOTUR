import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="labina82",
            database="ordenatotur"
        )
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    if conn.is_connected():
        conn.close()

conectar()
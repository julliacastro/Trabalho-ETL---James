import mysql.connector

class DBConnection:
    def __init__(self, host='localhost', user='root', password='your_password', database='your_database'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        cursor = conn.cursor()

        # Verificar se o banco de dados existe, senão, criar
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        
        cursor.close()
        conn.close()

        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return conn

    def close(self, conn):
        conn.close()

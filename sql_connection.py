import mysql.connector

def get_sql_connection():
     connection = mysql.connector.connect(user='root', password='S3g-tgXtwM@db',
                                host='127.0.0.1',
                                database='hospital_ms')
     return connection
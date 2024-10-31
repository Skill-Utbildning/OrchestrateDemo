import os
import cx_Oracle
import mysql.connector

def connect_oracle():
    try:
        connection = cx_Oracle.connect(
            user=os.environ.get('ORACLE_USER'),
            password=os.environ.get('ORACLE_PASSWORD'),
            dsn=os.environ.get('ORACLE_DSN')
        )
        print("Successfully connected to Oracle Database")
        return connection
    except cx_Oracle.Error as error:
        print(f"Error connecting to Oracle Database: {error}")
        return None

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE')
        )
        print("Successfully connected to MySQL Database")
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL Database: {error}")
        return None
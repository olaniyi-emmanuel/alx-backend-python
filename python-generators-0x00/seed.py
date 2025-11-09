
#connect application to MYSQLdatabase 

import mysql.connector 
import os 
from mysql.connector import Error 

def connect_db():
    try:
         connection  = mysql.connector.connect(
         host = 'localhost', 
         user = 'root', 
         password = 'app'  
)
         if connection.is_connected: 
              print("Database connected succesfully")
              return connection
    except Error as e:
         print(f"Database connection failed with the error {e}") 

         

def create_database(connection):
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS  ALX_prodev")


def connect_to_prodev():
        try:
             connection  = mysql.connector.connect(
                  host = 'localhost', 
                  user = 'root', 
                  password = 'app',
                  database = 'ALX_prodev'  )
             if connection.is_connected: 
                 print("Database connected succesfully")
                 return connection
        except Error as e:
         print(f"Database connection failed with the error {e}") 
        
def create_table(connection):
    mycursor = connection.cursor()
    mycursor.execute ("""
        CREATE TABLE IF NOT EXISTS  user_data( 
        user_id CHAR(36) PRIMARY KEY,           
        name VARCHAR(100) NOT NULL,             
        email VARCHAR(150) NOT NULL,             
        age DECIMAL(3,0) NOT NULL,                
        INDEX idx_user_id (user_id))         
        """) 
def insert_data(connection, data):
     csv_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3888260f107e3701e3cd81af49ef997cf70b6395.csv'
     mycursor = connection.cursor()
     mycursor.execute(f"""
     LOAD DATA INFILE '{csv_path}'
     INTO TABLE user_data
     FIELDS TERMINATED BY ','
     ENCLOSED BY '"' 
     LINES TERMINATED BY '\\n'
     IGNORE 1 ROWS 
     (@name, @email, @age) 
     SET user_id = UUID(),
     name = @name, 
     email = @email,
     age = @age;
     """)


if __name__ == "__main__":
    seed = __import__('seed')
    connection = seed.connect_db()
    if connection:
        seed.create_database(connection)
        connection.close()
        print(f"connection successful")

    connection = seed.connect_to_prodev()

    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        cursor = connection.cursor()
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print(f"Database ALX_prodev is present ")
        cursor.execute(f"SELECT * FROM user_data LIMIT 100;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()


     

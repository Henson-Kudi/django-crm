import mysql.connector

# connect to mysql
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '678560446-Hk'
)

# prepare the cursor object
cursor_object = database.cursor()

# create database
cursor_object.execute('CREATE DATABASE my_crm_clients')

print('Database created succesfully.')
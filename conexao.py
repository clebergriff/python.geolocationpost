import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="python",
    passwd="python",
    database='mercurio'
)
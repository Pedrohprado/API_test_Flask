import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="pedroprado123",
    database="testApiFlask"
)

mycursor= mydb.cursor()

mycursor.execute('INSERT INTO Olimpiada (cartao,name,Lider,Empresa) VALUES(5487,"Pedro Henrique","teste","Pedertractor")')


# mycursor.execute(
#     "CREATE TABLE Olimpiada (cartao INTEGER NOT NULL, name VARCHAR(255), Lider VARCHAR(255), Empresa VARCHAR(255), PRIMARY KEY(cartao))"
#     )
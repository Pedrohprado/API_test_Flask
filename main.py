from flask import Flask, make_response, jsonify, request
import mysql.connector as mysql


mydb = mysql.connect(
    host="localhost",
    user="root",
    password="pedroprado123",
    database="testApiFlask"
)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def getCarros():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM Olimpiada')
    olimpiadaGeral = mycursor.fetchall()

    funcionarios = list()
    for funcionario in olimpiadaGeral:
        funcionarios.append(
            {
                'cartao': funcionario[0],
                'name': funcionario[1],
                'lider': funcionario[2],
                'empresa': funcionario[3]
            }
        )

    return make_response(
        jsonify(
            mesage='Lista Olimpiada 2023',
            data=funcionarios
        )
    )


@app.route('/carros', methods=['POST'])
def createCarros():
    funcionaro = request.json

    mycursor = mydb.cursor()

    sql = f"INSERT INTO Olimpiada (cartao,name,Lider,Empresa) VALUES({funcionaro['cartao']},'{funcionaro['name']}','{funcionaro['lider']}','{funcionaro['empresa']}');"
    mycursor.execute(sql)

    mydb.commit()

    return make_response(
        jsonify(
            masage='Funcionario cadastrado',
            operator=funcionaro
        )
    )


@app.route('/carros', methods=['DELETE'])
def deleteCarros():
    funcionario = request.json

    mycursor = mydb.cursor()

    lookq = funcionario['cartao']

    # verif = f"SELECT * FROM Olimpiada WHERE cartao = {funcionario['cartao']}"
    # mycursor.execute(verif)
    
    mycursor.execute("DELETE FROM Olimpiada WHERE cartao = %s", [lookq])
    mydb.commit()
    print("Linha deletada com sucesso!")

app.run()

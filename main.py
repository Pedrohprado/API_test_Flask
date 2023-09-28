from flask import Flask, make_response, jsonify, request, render_template, flash, redirect
import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="pedroprado123",
    database="testApiFlask"
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = "@PEDROPRADO"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def sendInfoFuncionario():
    nome = request.form.get('name')
    card = request.form.get('cartao')
    lider = request.form.get('lider')
    empresa = request.form.get('empresa')
    nota = request.form.get('nota')

    if nome == '' and card == '':
        flash('Insira todas as informações')
    else:
        mycursor = mydb.cursor()

        sql = f"INSERT INTO Olimpiada (cartao,name,Lider,Empresa,nota) VALUES({card},'{nome}','{lider}','{empresa}',{nota})"
        mycursor.execute(sql)

        mydb.commit()
        return redirect('/')


@app.route('/funcionarios', methods=['GET'])
def getFuncionarios():
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
                'empresa': funcionario[3],
                'nota': funcionario[4]
            }
        )

    return make_response(
        jsonify(
            mesage='Lista Olimpiada 2023',
            data=funcionarios
        )
    )


# @app.route('/funcionarios', methods=['POST'])
# def createFuncionarios():
#     funcionaro = request.json

#     mycursor = mydb.cursor()

#     sql = f"INSERT INTO Olimpiada (cartao,name,Lider,Empresa) VALUES({funcionaro['cartao']},'{funcionaro['name']}','{funcionaro['lider']}','{funcionaro['empresa']}');"
#     mycursor.execute(sql)

#     mydb.commit()

#     return make_response(
#         jsonify(
#             masage='Funcionario cadastrado',
#             operator=funcionaro
#         )
#     )


@app.route('/remove', methods=['DELETE'])
def removeFuncionario():
    funcionario = request.json

    mycursor = mydb.cursor()

    lookq = funcionario['cartao']

    # verif = f"SELECT * FROM Olimpiada WHERE cartao = {funcionario['cartao']}"
    # mycursor.execute(verif)

    mycursor.execute("DELETE FROM Olimpiada WHERE cartao = %s", [lookq])
    mydb.commit()
    print("Linha deletada com sucesso!")


if __name__ == '__main__':
    app.run(debug=True)

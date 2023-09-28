from flask import Flask, make_response, jsonify, request, render_template, flash, redirect
import mysql.connector as mysql
import json

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


@app.route('/calculadora', methods=['POST'])
def calculadora():
    primeiroValor = int(request.form.get('firstQuest1'))
    segundoValor = int(request.form.get('secondQuest2'))
    terceiroValor = int(request.form.get('therdQuest3'))
    quartoValor = int(request.form.get('fortQuest4'))

    print(type(primeiroValor))

    total = (primeiroValor * 0.5) + (segundoValor * 1) + \
        (terceiroValor * 1.5) + (quartoValor * 2.75)
    return render_template('index.html', total=total)


@app.route('/register', methods=['POST'])
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
        return redirect('/funcionarios')


@app.route('/funcionarios', methods=['GET'])
def getFuncionarios():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM Olimpiada ORDER BY nota DESC')
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

    return render_template('index.html', funcionarios=funcionarios)


@app.route('/remove', methods=['POST'])
def remove():
    funcionario = request.form.get('deleta')
    print(funcionario)

    mycursor = mydb.cursor()
    verif = f"SELECT * FROM Olimpiada WHERE cartao = {funcionario}"

    mycursor.execute(verif)
    result = mycursor.fetchone()
    print(result)
    if result:
        mycursor.execute(
            "DELETE FROM Olimpiada WHERE cartao = %s", [funcionario])
        mydb.commit()
        return redirect('/funcionarios')
    else:
        return print("numero de cartão não encontrado")

# @app.route('/funcionarios', methods=['POST'])
# def createFuncionarios():
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


if __name__ == '__main__':
    app.run(debug=True)

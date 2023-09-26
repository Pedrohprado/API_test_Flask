from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response(
        jsonify(
            mesage='Lista de carros',
            data=Carros
        )
    )


@app.route('/carros', methods=['POST'])
def createCarros():
    carro = request.json
    Carros.append(carro)
    return carro


app.run()

import json
from flask_openapi3 import OpenAPI, Info
from flask import request

from core import Dado, PreProcessador, Modelo, Acuracia
from flask_cors import CORS

info = Info(title="Acuracia.io API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

@app.get('/')
def home():
    return "Execução OK da API."

@app.get('/carregar')
def carregar():
    dado = Dado()

    base = ('autismo5.csv')
    atributos = ['idade', 'ictericia','autismo_na_familia', 'resultado']

    dataset = dado.carregar(base, atributos)   
    return dataset.to_json(orient='values')


@app.get('/processar')
def processar():
    dado = Dado()
    pre_processador = PreProcessador()
    modelo = Modelo()
    acuracia = Acuracia()

    base = ('autismo5.csv')
    atributos = ['idade', 'ictericia','autismo_na_familia', 'resultado']
    dataset = dado.carregar(base, atributos)

    percentual_teste = 0.2  
    X_train, X_test, Y_train, Y_test = pre_processador.processar(dataset, percentual_teste)

    modelKNN = modelo.treinarKNN(X_train, Y_train)
    modelSVC = modelo.treinarSVC(X_train, Y_train)
    modelCART = modelo.treinarCART(X_train, Y_train)
    modelNB = modelo.treinarNB(X_train, Y_train)

    return json.dumps({
                                    'knn': acuracia.avaliar(modelKNN, X_test, Y_test), 
                                    'svc': acuracia.avaliar(modelSVC, X_test, Y_test),
                                    'cart': acuracia.avaliar(modelCART, X_test, Y_test),
                                    'nb': acuracia.avaliar(modelNB, X_test, Y_test)
                                })

@app.post('/adicionar')
def adicionar():
   data = request.data

   dado = Dado()
   base = ('autismo5.csv')
   dado.adicionar(base, data)
   
   return json.dumps({'error': 'false'})
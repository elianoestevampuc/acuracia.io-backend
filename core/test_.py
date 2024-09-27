from acuracia import Acuracia
from modelo import Modelo
from preProcessador import PreProcessador
from dado import Dado

def test_carregar_dados():
    dado = Dado()
    base = ('../autismo5.csv')
    atributos = ['idade', 'ictericia','autismo_na_familia', 'resultado']
    dataset = dado.carregar(base, atributos)

    assert len(dataset) == 704  

def test_acuracia():
    dado = Dado()
    pre_processador = PreProcessador()
    modelo = Modelo()
    acuracia = Acuracia()

    base = ('../autismo5.csv')
    atributos = ['idade', 'ictericia','autismo_na_familia', 'resultado']
    dataset = dado.carregar(base, atributos)

    percentual_teste = 0.2  
    X_train, X_test, Y_train, Y_test = pre_processador.processar(dataset, percentual_teste)
    model = modelo.treinarSVC(X_train, Y_train)
  
    assert acuracia.avaliar(model, X_test, Y_test) > 0.67    
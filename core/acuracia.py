from sklearn.metrics import accuracy_score

class Acuracia:

    def avaliar(self, modelo, X_test, Y_test):
        # Predição e avaliação do modelo
        predicoes = modelo.predict(X_test)
        return accuracy_score(Y_test, predicoes)
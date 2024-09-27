from sklearn.model_selection import train_test_split

class PreProcessador:

    def processar(self, dataset, percentual_teste, seed=7):
        # Divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.holdout(dataset,percentual_teste,seed)
        return (X_train, X_test, Y_train, Y_test)

    def holdout(self, dataset, percentual_teste, seed):
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)
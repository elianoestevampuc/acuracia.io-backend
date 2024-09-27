from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

class Modelo:

    def treinarKNN(self, X_train, Y_train):
        modelo = KNeighborsClassifier()
        modelo.fit(X_train, Y_train)
        return modelo  
    
    def treinarSVC(self, X_train, Y_train):
        modelo = SVC()
        modelo.fit(X_train, Y_train)
        return modelo
          
    def treinarCART(self, X_train, Y_train):
        modelo = DecisionTreeClassifier()
        modelo.fit(X_train, Y_train)
        return modelo     
    
    def treinarNB(self, X_train, Y_train):
        modelo = GaussianNB()
        modelo.fit(X_train, Y_train)
        return modelo   
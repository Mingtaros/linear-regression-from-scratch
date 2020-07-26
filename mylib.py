import numpy as np

class MyLinearRegression:
    def __init__(self):
        self.theta = None
        
    def fit(self, X,y):
        # spesifikasi: method untuk melakukan training, yaitu fitting modelnya ke X dan y

        # menambahkan satu kolom baru yang berisikan full 1, sebagai pengali bias 
        Xtemp = X.copy()    
        Xtemp['bias'] = 1

        # normal equation untuk mencari theta
        Xtranspose = Xtemp.T
        self.theta = np.linalg.inv(Xtranspose.dot(Xtemp)).dot(Xtranspose).dot(y)
        
    def predict(self, X):
        # spesifikasi: method untuk melakukan prediksi

        # menambahkan satu kolom baru yang berisikan full 1, sebagai pengali bias 
        Xtemp = X.copy()
        Xtemp['bias'] = 1

        # prediksi dengan menggunakan theta yang telah di fit sebelumnya, kemudian dikalikan dengan X yang akan di predict
        return Xtemp.dot(self.theta)
    
    def getTheta(self):
        # spesifikasi: method untuk mereturn theta

        return self.theta


'''
# CARA PENGGUNAAN

from mylib import MyLinearRegression
myLinearRegression = new MyLinearRegression()
myLinearRegression.fit(X_train, y_train)        # fit training dataset
myLinearRegression.predict(X_test)              # predict test dataset

'''
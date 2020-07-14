import numpy as np

class MyLinearRegression:
    def __init__(self):
        self.theta = None
        
    def fit(self, X,y):
        Xtemp = X.copy()
        Xtemp['bias'] = 1
        self.theta = np.linalg.inv(Xtemp.T.dot(Xtemp)).dot(Xtemp.T).dot(y)
        
    def predict(self, X):
        Xtemp = X.copy()
        Xtemp['bias'] = 1
        return Xtemp.dot(self.theta)
    
    def getTheta(self):
        return self.theta
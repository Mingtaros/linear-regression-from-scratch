import pandas as pd
import numpy as np

class LinearRegression:
    def __init__(self, data):
        self.data = data
        self.attribute = []
        self.target = ''
        self.model = []
        self.dataTest = []
    
    def setAttribute(self, listAttribute):
        self.attribute = listAttribute

    def setTarget(self, attribute) :
        self.target = attribute
    
    def setDataTrain(self, dataTrain) :
        self.data = dataTrain
    
    def setDataTest(self, dataTest) :
        self.dataTest = dataTest
    
    def sum(self, attribute) :
        dataAttribute = self.data[attribute]
        res = 0
        for i in range(len(self.data.index)) :
            res += dataAttribute[i]
        return res
    
    def sumprod(self, a, b) :
        dataA = self.data[a]
        dataB = self.data[b]
        return dataA.dot(dataB)
    
    def train(self) :
        tmpTarget = [0 for i in range(0, len(self.attribute) + 1)]
        tmpTarget[0] = self.sum(self.target)
        for i in range(len(self.attribute)) :
            tmpTarget[i + 1] = self.sumprod(self.attribute[i], self.target)
        
        tmp = [[0 for i in range(len(self.attribute)+1)] for i in range(len(self.attribute)+1)]
        for i in range(len(self.attribute) + 1) :
            for j in range(len(self.attribute) + 1) :
                if i == 0 :
                    if j == 0 :
                        tmp[i][j] = len(self.data.index)
                    else :
                        tmp[i][j] = self.sum(self.attribute[j-1])
                else :
                    if j == 0 :
                        tmp[i][j] = self.sum(self.attribute[i-1])
                    else :
                        tmp[i][j] = self.sumprod(self.attribute[i-1], self.attribute[j-1])
        
        A = np.array(tmp)
        B = np.array(tmpTarget)
        self.model = np.linalg.inv(A).dot(B)
    
    def test(self) :
        result = [0 for i in range(len(self.dataTest.index))]

        arr = [self.dataTest.loc[:,[self.attribute[i]]].values.tolist() for i in range(len(self.attribute))]
        
        for i in range(len(self.model)) :
            for j in range(len(self.dataTest.index)) :
                if i == 0 :
                    result[j] = self.model[i]
                else :
                    result[j] += self.model[i] * arr[i-1][j][0]

        sum = 0
        targetValue = self.dataTest.loc[:, [self.target]].values.tolist()
        for i in range(len(self.dataTest.index)) :
            error = abs(result[i] - targetValue[i][0])
            sum += error
        
        mean_absolute_error = sum / len(self.dataTest.index)

        # print(result)
        print("Mean absolute error : ", end="")
        print(mean_absolute_error)
        return mean_absolute_error
            

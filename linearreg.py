import numpy as np

class MyLinearRegression:
    def __init__(self, inputD=1, outputD=1, learningRate=0.005):
        # weight is the vector of gradient that will be regressed through training
        self.weight = np.zeros((outputD,inputD))
        # bias is the intercept
        self.bias = np.zeros((1,outputD))
        # learning_rate is the multiplier of changes in every iteration
        self.learning_rate = learningRate

    def train(self, data, label=None, iteration=20):
        if not label.any():
            label_train = data[:,-1]
            data_train = data[:,:-1]
        else:
            label_train = label
            data_train = data
        for _ in range(iteration):
            for sample, label in zip(data_train,label_train):
                #============EXPLANATION=============================================================#
                # y^ is hypothesis (label), y is for the real value (label)                                                                  #                                            
                # every iteratiorn, the weight will be updated                                                                                #                               
                # weight will be updated by dLoss/dweight, where Loss is calculated using                                    #                                                                            
                #     Mean Squared Error = (1/N sigma (i : [1..n] (yi - y^i) ** 2))                                                       #                                                       
                #         Where N is the output vector length, in cases where Y is single valued it is a normal float  #                                                                                                              
                # dL/dw = dL/d y^ * d y^/dw                                                                                                             #       
                #     where dL/dy^ = dL/d(y - y^) * d(y-y^)/dy^                                                                                 #                                
                #     where d(y-y^)/dy^ = -1 and dL/d(y -y^) = 2 * (y-y^), therefore dL/dy^ = -2 * (y - y^)              #                                                                                                 
                #     since y^  = features . weight + bias , therefore dy^/dw = features                                           #                                                                       
                # therefore dL/dw = -2 * (y - y^) * features                                                                                   #                               
                # new weight = old weight - learnrate * dL/dw                                                                                 #                                
                #========================================================================================#
                hypothesis = np.dot(self.weight,sample) + self.bias
                self.weight -= (self.learning_rate / len(self.weight)) * -2 * (np.dot((label-hypothesis).reshape(-1,1),sample.reshape(1,-1)))
                self.bias -= (self.learning_rate * -2) * (label - hypothesis)
        

    def trainandtest(self,data,iteration):
        self.train(data[:len(data)-(len(data)/4)],iteration)
        for i in range((len(data)*3/4),len(data)):
            print("Hypothesis : ")
            print(np.dot(data[i,:-1],self.weight) + self.bias)
            print("Observed : ")
            print(data)


#dibawah ini cuma buat testing
def func1(data,noise):
    tot = 0
    for i in range(len(data)):
        tot += (i+1)*data[i]
    if noise:
        if i %  4 == 1:
            tot += noise*np.random.rand()*np.random.randint(-1,1)
    return tot
def func2(data,noise):
    tot = 0
    for i in range(len(data)):
        tot += (len(data) - i)*data[i]
    if noise:
        if i %  4 == 1:
            tot += noise*np.random.rand()*np.random.randint(-1,1)
    return tot


def generateTestCase(N,xnum,ydim,noise=0):
    # print(noise)
    testdata = []
    labeldata = []
    for k in range(N):
        data = np.random.randint(1,10,(xnum))
        label = np.zeros((ydim))
        for i in range(ydim):
            if i % 2 == 1:
                label[i] = func1(data,noise)
            else:
                label[i] = func2(data,noise)
        testdata.append(data)
        labeldata.append(label)
        # np.append(testdata[-1],label)
    return np.array(testdata),np.array(labeldata)

if __name__ == '__main__':
        obj = MyLinearRegression(3,1,0.005)
        x,y = generateTestCase(8,3,1,noise=5)
        # print(x)
        # print(y) 
        obj.train(x,label=y,iteration=100)
        print(obj.weight)


        
    

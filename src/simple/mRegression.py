# regression.py
# Contain all module to process certain data to get the regression linear

class Regression:
    # Constructor to create new Regression object
    def __init__(self, matX, arrY, N, k):
        self.matX = matX
        self.arrY = arrY
        self.b = None
        self.N = N
        self.k = k

    # Process all arrX and arrY data to get regression linear equation
    def run(self):
        Matrix = self.generate_Linear_Equation()
        print(Matrix)
        self.solve_Equation(Matrix)
        self.showRegression()

    # Show regression equation
    def showRegression(self):
        rest = ''
        for i in range(1, self.k + 1):
            if (self.b[i] >= 0):
                rest = rest + " + " + str(self.b[i]) + "x" + str(i)
            else:
                rest = rest + " - " + str(-self.b[i]) + "x" + str(i)
        result = "y_hat = " + str(self.b[0]) + rest
        print(result)

    # Test the regression with test dataset
    def test(self, testFrame, testY):
        numOfData = len(testFrame[0])
        YHat = self.compute_YHat(testFrame, numOfData)
        print("#\t\t",end='')
        for i in range(len(testFrame)):
            print("X"+str(i+1)+"\t\t",end='')
        print("Y\t\t YHat")
        for i in range(numOfData):
            result = str(i+1) + "\t\t"
            for j in range(len(testFrame)):
                result = result + str(testFrame[j][i]) + "\t\t"
            result = result + str(testY[i]) + "\t\t"
            result = result + str(YHat[i])
            print(result)
        print("Regression Accuracy =",self.compute_RSquare(testY, YHat))

    # Compute the predicted value Y from regression value from X
    def regression_Value(self, P):
        sum = 0
        for i in range(1, self.k + 1):
            sum += self.b[i] * P[i-1]
        return self.b[0] + sum

    # Compute Y Hat value for each X Test value
    def compute_YHat(self, testX, numOfData):
        testYHat = []
        for i in range(numOfData):
            P = []
            for j in range(1, self.k + 1):
                P.append(testX[j-1][i])
            testYHat.append(self.regression_Value(P))
        return testYHat

    # Sum all value of array arr
    def sum_Array_Data(self, arr):
        sum = 0
        for data in arr:
            sum += data
        return sum

    # Sum all multiplied of array A and array B
    def sum_Multiply_Data(self, A, B):
        sum = 0
        for i in range(self.N):
            sum += A[i] * B[i]
        return sum

    # Generate all linear equation
    def generate_Linear_Equation(self):
        Matrix = []
        # Compute left-value
        for i in range(0, self.k + 1):
            Row = []
            for j in range(0, self.k + 1):
                result = 0
                if ((i == 0) and (j == 0)):
                    result = self.N
                elif (i == 0):
                    result = self.sum_Array_Data(self.matX[j-1])
                elif (j == 0):
                    result = self.sum_Array_Data(self.matX[i-1])
                else:
                    result = self.sum_Multiply_Data(self.matX[i-1], self.matX[j-1])
                Row.append(result)
            Matrix.append(Row)
        
        # Compute right-value
        for i in range(0, self.k + 1):
            if (i == 0):
                result = self.sum_Array_Data(self.arrY)
            else:
                result = self.sum_Multiply_Data(self.matX[i-1], self.arrY)
            Matrix[i].append(result)

        return Matrix

    # Compute all linear equation to get b0, b1, ..., bN
    def solve_Equation(self, M):
        n = self.k + 1
        for j in range(0, n):
            for i in range(0, n):
                if (i != j):
                    c = M[i][j] / M[j][j]
                    for k in range (0, n+1):
                        M[i][k] = M[i][k] - c * M[j][k]
        
        b = [0 for i in range(0, n)]
        for i in range(0, n):
            b[i] = M[i][n] / M[i][i]
        
        self.b = b

    # Return the mean of all data
    def getMean(self, arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return sum / len(arr)

    # Compute least square estimation  or sum square of error (SSE)
    def compute_SSE(self, realY, hatY):
        sum = 0
        for i in range(len(realY)):
            sum += (realY[i] - hatY[i]) ** 2
        return sum
    
    # Compute sum square of total
    def compute_SST(self, realY):
        sum = 0
        y_mean = self.getMean(realY)
        for i in range(len(realY)):
            sum += (realY[i] - y_mean) ** 2
        return sum

    # Compute the coefficient of determination
    def compute_RSquare(self, realY, hatY):
        SSE = self.compute_SSE(realY, hatY)
        SST = self.compute_SST(realY)
        return 1 - (SSE / SST)

matX = [[0, 10, 20, 30, 40]]
arrY = [30, 40, 50, 60, 70]
N = len(arrY)
k = len(matX)

Reg = Regression(matX, arrY, N, k)
Reg.run()
Reg.test(matX, arrY)
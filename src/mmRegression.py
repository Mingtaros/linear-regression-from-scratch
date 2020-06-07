# regression.py
# Contain all module to process certain data to get the regression linear

class Regression:
    # Constructor to create new Regression object
    def __init__(self, matX, matY, N, k):
        self.matX = matX
        self.matY = matY
        self.matB = []
        self.N = N
        self.k = k

    # Process all arrX and arrY data to get regression linear equation
    def run(self):
        for i in range(len(self.matY)):
            Matrix = self.generate_Linear_Equation(self.matY[i])
            self.solve_Equation(Matrix)
            self.showRegression(i)

    # Show regression equation
    def showRegression(self, l):
        rest = ''
        for i in range(1, self.k + 1):
            if (self.matB[l][i] >= 0):
                rest = rest + " + " + str(self.matB[l][i]) + "x" + str(i)
            else:
                rest = rest + " - " + str(-self.matB[l][i]) + "x" + str(i)
        result = "y_hat = " + str(self.matB[l][0]) + rest
        print(result)

    # Test the regression with test dataset
    def test(self, testFrame, testY):
        numOfData = len(testFrame[0])
        for l in range(len(testY)):
            YHat = self.compute_YHat(testFrame, numOfData, l)
            print("#\t\t",end='')
            for i in range(len(testFrame)):
                print("X"+str(i+1)+"\t\t",end='')
            print("Y\t\t YHat")
            for i in range(numOfData):
                result = str(i+1) + "\t\t"
                for j in range(len(testFrame)):
                    result = result + str(testFrame[j][i]) + "\t\t"
                result = result + str(testY[l][i]) + "\t\t"
                result = result + str(YHat[i])
                print(result)
            print("Regression Accuracy =",self.compute_RSquare(testY[l], YHat))

    # Compute the predicted value Y from regression value from X
    def regression_Value(self, P, l):
        sum = 0
        for i in range(1, self.k + 1):
            sum += self.matB[l][i] * P[i-1]
        return self.matB[l][0] + sum

    # Compute Y Hat value for each X Test value
    def compute_YHat(self, testX, numOfData, l):
        testYHat = []
        for i in range(numOfData):
            P = []
            for j in range(1, self.k + 1):
                P.append(testX[j-1][i])
            testYHat.append(self.regression_Value(P, l))
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
    def generate_Linear_Equation(self, arrY):
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
                result = self.sum_Array_Data(arrY)
            else:
                result = self.sum_Multiply_Data(self.matX[i-1], arrY)
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

        self.matB.append(b)

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
arrY = [[31, 32, 47, 79, 89],[30, 40, 50, 60, 70]]

N = len(arrY[0])
k = len(matX)
print(k)

Reg = Regression(matX, arrY, N, k)
Reg.run()
Reg.test(matX, arrY)
print(Reg.matB[0])
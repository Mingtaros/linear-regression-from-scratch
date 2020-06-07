# regression.py
# Contain all module to process certain data to get the regression linear

class Regression:
    # Constructor to create new Regression object
    def __init__(self, arrX, arrY, N):
        self.arrX = arrX
        self.arrY = arrY
        self.arrYHat = None
        self.N = N
        self.b0 = 0
        self.b1 = 0

    # Process all arrX and arrY data to get regression linear equation
    def run(self):
        self.compute_b1()
        print("b1 =",self.b1)
        self.compute_b0()
        print("b0 =",self.b0)
        self.showRegression()
        self.compute_YHat()
        print("Regression Accuracy =",self.compute_RSquare())

    # Compute all regression value from testFrame
    def test(self, XTest, YTest):
        YHat = []
        print("#\t X\t\t Y\t\t Y prediction")
        for i in range(len(XTest)):
            YHat.append(self.regression_Value(XTest[i]))
            print(str(i+1) + "\t " + str(XTest[i]) + "\t\t " + str(YTest[i]) + "\t\t " + str(YHat[i]))
        return YHat

    # Show regression equation
    def showRegression(self):
        if (self.b1 >= 0):
            slope = " + " + str(self.b1) + "x"
        else:
            slope = " - " + str(-self.b1) + "x"
        result = "y_hat = " + str(self.b0) + slope
        print(result)

    # Compute b0 value from regression b0 formula
    def compute_b0(self):
        numerator = self.sum_Y_Data() - self.b1 * self.sum_X_Data()
        denominator = self.N
        self.b0 = numerator / denominator

    # Compute b1 value from regression b1 formula
    def compute_b1(self):
        numerator = self.N * self.sum_Multiply_Data() - self.sum_X_Data() * self.sum_Y_Data()
        denominator = self.N * self.sum_Square_X_Data() - (self.sum_X_Data() ** 2)
        self.b1 = numerator / denominator

    # Sum all value of data arrX
    def sum_X_Data(self):
        sum = 0
        for data in self.arrX:
            sum += data
        return sum

    # Sum all value of data arrY
    def sum_Y_Data(self):
        sum = 0
        for data in self.arrY:
            sum += data
        return sum

    # Sum all square value of data arrX
    def sum_Square_X_Data(self):
        sum = 0
        for data in self.arrX:
            sum += data ** 2
        return sum

    # Sum all square value of data arrY
    def sum_Square_Y_Data(self):
        sum = 0
        for data in self.arrY:
            sum += data ** 2
        return sum

    # Sum all multiplied data X and data Y
    def sum_Multiply_Data(self):
        sum = 0
        for i in range(self.N):
            sum += self.arrX[i] * self.arrY[i]
        return sum

    # Compute the predicted value Y from regression value from X
    def regression_Value(self, X):
        return self.b0 + self.b1 * X

    # Getter for B0 value based on y_hat = B0 + B1x
    def getB0(self):
        return self.b0

    # Getter for B1 value based on y_hat = B0 + B1x
    def getB1(self):
        return self.b1

    # Return the mean of all data
    def getMean(self, arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return sum / len(arr)

    # Compute Y Hat value for each X Value
    def compute_YHat(self):
        self.arrYHat = []
        for i in range(len(self.arrX)):
            self.arrYHat.append(self.regression_Value(self.arrX[i]))

    # Compute least square estimation  or sum square of error (SSE)
    def compute_SSE(self):
        sum = 0
        for i in range(len(self.arrY)):
            sum += (self.arrY[i] - self.arrYHat[i]) ** 2
        return sum
    
    # Compute sum square of total
    def compute_SST(self):
        sum = 0
        y_mean = self.getMean(self.arrY)
        for i in range(len(self.arrY)):
            sum += (self.arrY[i] - y_mean) ** 2
        return sum

    # Compute the coefficient of determination
    def compute_RSquare(self):
        SSE = self.compute_SSE()
        SST = self.compute_SST()
        return 1 - (SSE / SST)
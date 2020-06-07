# dataloader.py
# Load .csv data to program variables

import pandas as pd

class Loader:
    # Constructor to create new Loader object
    def __init__(self, fileName, splitFactor):
        self.fileName = fileName
        self.splitFactor = splitFactor
        self.dataFrame = None
        self.trainFrame = None
        self.testFrame = None
        self.midpoint = 0
        self.x_columns = []
        self.y_columns = []

    # Execute loader
    def run(self):
        self.dataFrame = pd.read_csv("../data/" + self.fileName)
        print(self.dataFrame)
        self.split_dataFrame()

        input()
        all_cols = self.get_All_Column()
        print("All column: ")
        for i in range(len(all_cols)):
            print(str(i+1)+". "+all_cols[i])
        print()
        
        num_cols = self.get_Numeric_Columns()
        print("Numeric column: ")
        for i in range(len(num_cols)):
            print(str(i+1)+". "+num_cols[i])
        print()
        print("Enter how many y-variable and x-variable: ")
        n = int(input("X variable: "))
        m = int(input("Y variable: "))
        for i in range(n):
            print(str(i+1), end=' ')
            selectedColumn = input()
            self.x_columns.append(selectedColumn)
        for i in range(m):
            print(str(i+1), end=' ')
            selectedColumn = input()
            self.y_columns.append(selectedColumn)
    
    # Split dataframe into trainFrame and testFrame
    def split_dataFrame(self):
        size = len(self.dataFrame)
        self.midpoint = int(round(size * self.splitFactor))
        self.trainFrame = self.dataFrame[0: self.midpoint]
        self.testFrame = self.dataFrame[self.midpoint: size]
        print(self.trainFrame)
        print(self.testFrame)

    # Get all column of the dataframe
    def get_All_Column(self):
        result = []
        for column in self.dataFrame.columns:
            result.append(column)
        return result

    # Get numeric columns of the dataframe
    def get_Numeric_Columns(self):
        result = []
        dfTemp = self.dataFrame.select_dtypes(include=['float64', 'int64'])
        for column in dfTemp.columns:
            result.append(column)
        return result

    # Get all train x_columns dataset value
    def get_X_train(self):
        matX = []
        for i in range(len(self.x_columns)):
            arrX = []
            for j in range(len(self.trainFrame[self.x_columns[i]])):
                arrX.append(self.trainFrame[self.x_columns[i]].get(j))
            matX.append(arrX)
        return matX

    # Get all train y_columns dataset value
    def get_Y_train(self):
        matY = []
        for i in range(len(self.y_columns)):
            arrY = []
            for j in range(len(self.trainFrame[self.y_columns[i]])):
                arrY.append(self.trainFrame[self.y_columns[i]].get(j))
            matY.append(arrY)
        return matY

    # Get all test x_columns dataset value
    def get_X_test(self):
        matX = []
        for i in range(len(self.x_columns)):
            arrX = []
            for j in range(len(self.testFrame[self.x_columns[i]])):
                arrX.append(self.testFrame[self.x_columns[i]].get(j+self.midpoint))
            matX.append(arrX)
        return matX

    # Get all test y_columns dataset value
    def get_Y_test(self):
        matY = []
        for i in range(len(self.y_columns)):
            arrY = []
            for j in range(len(self.testFrame[self.y_columns[i]])):
                arrY.append(self.testFrame[self.y_columns[i]].get(j+self.midpoint))
            matY.append(arrY)
        return matY

    # Get x-column name
    def get_x_column(self, i):
        return self.x_columns[i]

    # Get y-column name
    def get_y_column(self, i):
        return self.y_columns[i]
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
        self.x_column = ''
        self.y_column = ''

    # Execute loader
    def run(self):
        self.dataFrame = pd.read_csv("../data/" + self.fileName)
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
        print("Select two column as x and y variable: ")
        self.x_column = input("X variable: ")
        self.y_column = input("Y variable: ")
    
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

    # Get X-Array train value
    def get_arrX_train(self):
        arrX = []
        for i in range(len(self.trainFrame[self.x_column])):
            arrX.append(self.trainFrame[self.x_column].get(i))
        return arrX

    # Get Y-Array train value
    def get_arrY_train(self):
        arrY = []
        for i in range(len(self.trainFrame[self.y_column])):
            arrY.append(self.trainFrame[self.y_column].get(i))
        return arrY

    # Get X-Array test value
    def get_arrX_test(self):
        arrX = []
        for i in range(len(self.testFrame[self.x_column])):
            arrX.append(self.testFrame[self.x_column].get(i+self.midpoint))
        return arrX

    # Get Y-Array test value
    def get_arrY_test(self):
        arrY = []
        for i in range(len(self.testFrame[self.y_column])):
            arrY.append(self.testFrame[self.y_column].get(i+self.midpoint))
        return arrY

    # Get x-column name
    def get_x_column(self):
        return self.x_column

    # Get y-column name
    def get_y_column(self):
        return self.y_column
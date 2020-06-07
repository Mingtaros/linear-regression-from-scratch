# main.py
# Main Program for Linear Regression Generator
# Linear Regression from Scratch

from regression import *
from dataloader import *
from visualizer import *

# Main Program or Driver for Linear Regression From Scratch
print("Sthyrelest Enterprise - Linear Regression Generator")
print("Probability and Statistics - Linear Regression")
print("Created by: 13518056 - Michael Hans", end='\n\n')

print("There are three sections in this program:")
print("1. Input and Loader")
print("2. Regression")
print("3. Testing and Visualizing", end='\n\n')

print("Welcome to the Linear Regression Generator!", end='\n\n')

# ==============================================================================================
# Section 1 : Input and Loader
# ==============================================================================================
print("Section 1 : Input and Loader", end='\n\n')
fileName = input("Input the name of the dataset file: ")
isSuccess = False
while (not(isSuccess)):
    splitFactor = float(input("Please enter split factor value between 0 and 1: "))
    isSuccess = (splitFactor > 0) and (splitFactor < 1)

Ldr = Loader(fileName, splitFactor)
Ldr.run()
print()

# ==============================================================================================
# Section 2 : Regression
# ==============================================================================================
print("Section 2 : Regression", end='\n\n')
XTrain = Ldr.get_arrX_train()
YTrain = Ldr.get_arrY_train()
XTest = Ldr.get_arrX_test()
YTest = Ldr.get_arrY_test()

Reg = Regression(XTrain, YTrain, len(XTrain))
Reg.run()
print()

# ==============================================================================================
# Section 3 : Testing and Visualizing
# ==============================================================================================
print("Section 3 : Testing and Visualizing", end='\n\n')
print("Regression Equation:")
Reg.showRegression()
print()
print("Testing the regression line with Testing Data")
YHat = Reg.test(XTest, YTest)
b0 = Reg.getB0()
b1 = Reg.getB1()

print()
print("Visualizing..")
Visualize(XTrain, YTrain, XTest, YTest, YHat, b0, b1, Ldr.get_x_column(), Ldr.get_y_column())
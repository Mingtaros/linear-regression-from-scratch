# main.py
# Main Program for Linear Regression Generator
# Linear Regression from Scratch

from mmRegression import *
from mDataloader import *
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
# print("Section 1 : Input and Loader", end='\n\n')
# fileName = input("Input the name of the dataset file: ")
# isSuccess = False
# while (not(isSuccess)):
#     splitFactor = float(input("Please enter split factor value between 0 and 1: "))
#     isSuccess = (splitFactor > 0) and (splitFactor < 1)

Ldr = Loader("car_data.csv", 0.8)
Ldr.run()
print()

# ==============================================================================================
# Section 2 : Regression
# ==============================================================================================
print("Section 2 : Regression", end='\n\n')
XTrain = Ldr.get_X_train()
YTrain = Ldr.get_Y_train()
XTest = Ldr.get_X_test()
YTest = Ldr.get_Y_test()
N = len(XTrain)
M = len(YTrain)

Reg = Regression(XTrain, YTrain, len(XTrain[0]), len(XTrain))
Reg.run()
print()

# ==============================================================================================
# Section 3 : Testing and Visualizing
# ==============================================================================================
print("Section 3 : Testing and Visualizing", end='\n\n')
print("Regression Equation:")
for i in range(M):
    Reg.showRegression(i)
print()
print("Testing the regression line with Testing Data")
Reg.test(XTest, YTest)
# b0 = Reg.getB0()
# b1 = Reg.getB1()

print()

print("Visualizing..")
for i in range(N):
    for j in range(M):
        RegViz = Regression([XTrain[i]], [YTrain[j]], len(XTrain[0]), 1)
        RegViz.run()
        Visualize(XTrain[i], YTrain[j], XTest[i], YTest[j], RegViz.matB[0][0], RegViz.matB[0][1], Ldr.get_x_column(i), Ldr.get_y_column(j))
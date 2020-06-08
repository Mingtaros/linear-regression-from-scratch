# visualizer.py
# Module to visualize the map and the streets in complex way
# The visualization is using matplotlib library

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Plot a point on workspace
def Plotting(x, y, k):
    # If (x,y) is the train point
    if (k == 1):
        plt.plot([x], [y], 'ro', color = "blue")

    # If (x,y) is the test point
    elif (k == 2):
        plt.plot([x], [y], 'ro', color = "red")

    # If (x,y) is the predicted point
    elif (k == 3):
        plt.plot([x], [y], 'ro', color = "black")

    # label = "(%f,%f)" % (x, y)
    # plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# Visualize the dataframe with the regression line and value
def Visualize(XTrain, YTrain, XTest, YTest, B0, B1, XLabel, YLabel):
    # Determine x-range with xmin and xmax based on dataframe
    xmin = min(XTrain)
    candidate = min(XTest)
    if (xmin > candidate):
        xmin = candidate

    xmax = max(XTrain)
    candidate = max(XTest)
    if (xmax < candidate):
        xmax = candidate

    # Visualize every train value in dataframe with blue color
    for i in range(len(XTrain)):
        Plotting(XTrain[i], YTrain[i], 1)

    # Visualize every test value in dataframe with red color
    for i in range(len(XTest)):
        Plotting(XTest[i], YTest[i], 2)

    # Visualize regression line with green color
    x = np.linspace(xmin, xmax, 10)
    plt.plot(x, B0 + B1*x, '-g', label='hoiii')  # solid green

    # Create legend information
    legendNote = []
    colors = ['blue', 'red', 'black', 'green']
    labels = ['Train value', 'Test value', 'Predicted value', 'Regression Line']
    for i in range(4):
        legendNote.append(mpatches.Patch(color=colors[i], label=labels[i]))
    plt.legend(handles=legendNote)

    plt.axis('equal')
    plt.title('Simple Regression Linear')
    plt.xlabel(XLabel)
    plt.ylabel(YLabel)
    plt.show()
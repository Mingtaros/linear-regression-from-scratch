import pandas as pd
import numpy as np
import math

def hitungKoefisien(x,y):
    # B = (invers(X'X))*(X'Y)
    a = x.transpose() # X'
    b = np.dot(a, x) # X'X
    c = np.linalg.inv(b) # invers(X'X)
    d = np.dot(a, y) # X'Y
    res = np.dot(c, d)
    return res

def prediksiY(xbaru, koef):
    # Y = x * koef + e
    res = [[0 for i in range(len(koef[0]))] for j in range(len(xbaru))]
    for i in range(len(xbaru)):
        for j in range(len(koef[0])):
            for k in range(len(koef)):
                res[i][j] += xbaru[i][k]*koef[k][j]
    return res

def hitungSSE(yreal,yestimate):
    # SSE = sum((yreal - yestimate)^2)
    res = 0
    for i in range(len(yreal)):
        res += math.pow(yreal[i]-yestimate[i], 2)
    return res

def hitungSST(yreal):
    # SST = sum((yreal - yrata2)^2)
    hasil = 0
    ymean = np.mean(yreal)
    for i in range(len(yreal)):
        hasil += math.pow((yreal[i]-ymean), 2)
    return hasil

def hitungRsquare(yreal,yestimate):
    # R = (1-(sse/sst))
    return(1-(hitungSSE(yreal, yestimate)/hitungSST(yreal)))
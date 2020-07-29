import numpy as np
import math


def multipleLinearRegression(xPredict, x, y):
    # mengembalikan hasil prediksi dari inputan data x
    # xPredict=[1,x1,x2,x3,..]
    return(multiplyMatrix(xPredict, koefRegression(x, y)))


def koefRegression(x, y):
    # mengembalikan array of koefisien (B)
    # x merupakan matriks nx(p+1), dimana p adalah jumlah var bebas (independent variables)
    # y merupakan matriks nx1
    # B = (invers(X'X))*(X'Y)
    xTrans = np.transpose(x)
    inverse = np.linalg.inv(multiplyMatrix(xTrans, x))
    xTransy = multiplyMatrix(xTrans, y)
    B = multiplyMatrix(inverse, xTransy)
    return B


def multiplyMatrix(a, b):
    # mengembalikan matriks hasil perkalian a*b
    # asumsi : dimensi matriks bisa dikalikan
    # matriks hasil
    hasil = [[0 for i in range(len(b[0]))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                hasil[i][j] += a[i][k]*b[k][j]

    return hasil


def SSE(yreal, yestimate):
    # mengembalikan hasil dari sum square of error dari data yreal dan yestimate
    # inisialisasi hasil
    hasil = 0
    for i in range(len(yreal)):
        selisih = yreal[i]-yestimate[i]
        hasil += math.pow(selisih, 2)

    return hasil


def SST(yreal):
    # mengembalikan hasil dari sum square of total dari data yreal
    # cari avg dari data terlebih dahulu
    yavg = np.mean(yreal)
    # inisialisasi hasil
    hasil = 0
    for i in range(len(yreal)):
        selisih = yreal[i]-yavg
        hasil += math.pow(selisih, 2)
    return hasil


def kualitasRegresi(yreal, yestimate):
    sse = SSE(yreal, yestimate)
    sst = SST(yreal)
    return(1-(sse/sst))

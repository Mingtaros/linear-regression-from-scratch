import numpy as np


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

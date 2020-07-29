import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def processCSV(filename):
    #Parsing csv
    df = pd.read_csv(filename, delimiter=",")

    df["Kms_Driven/100"] = df["Kms_Driven"]/100
    df["Age"] = 2018 - df["Year"]
    #Olah data yang bukan int/float
    # Petrol -> 0
    # Diesel -> 1
    # CNG -> 2
    df["Fuel_Type"] = pd.factorize(df["Fuel_Type"])[0]
    df["Seller_Type"] = pd.factorize(df["Seller_Type"])[0]
    df["Transmission"] = pd.factorize(df["Transmission"])[0]

    return df

def splitTestTrain(df, percentage):
    return train_test_split(df, test_size = percentage)

def splitVar(df, x_name, y_name):

    x = np.c_[np.ones((df.shape[0], 1)), df[x_name].to_numpy()]
    y = df[y_name].to_numpy()
    
    return x, y

def calcCoeff(x_var, y_var):
    xt_var = x_var.transpose()
    a_var = np.dot(xt_var, x_var)
    ai_var = np.linalg.inv(a_var)
    b_var = np.dot(xt_var, y_var)

    res = np.dot(ai_var, b_var)
    return res

def predict(x_var, coef):
    res = [0 for i in range(x_var.shape[0])]

    for i in range (x_var.shape[0]):
        for j in range(x_var.shape[1]):
            res[i] += x_var[i][j] * coef[j]

    return res

def calc_res(y_var, pred):
    return [y_var[i] - pred[i] for i in range(y_var.shape[0])]

def calc_variance(y_var):
    y_mean = np.sum(y_var)/y_var.shape[0]
    return [y - y_mean for y in y_var]

def calc_ssres(y_var, pred):
    residuals = calc_res(y_var, pred)
    return np.sum([res**2 for res in residuals])

def calc_ssvar(y_var):
    variances = calc_variance(y_var)
    return np.sum([var**2 for var in variances])

def calc_rsquared(y_var, pred):
    ssres = calc_ssres(y_var, pred)
    ssvar = calc_ssvar(y_var)

    print("SSE = {:.4f}".format(ssres))
    print("SST = {:.4f}".format(ssvar))
    return 1 - (ssres/ssvar)


def drawReg(x_test, y_test, coef, option, x_legend, y_legend):
    plt.scatter(x_test.transpose()[option], y_test.transpose(), c='red')
    y = coef[0][0] + coef[option][0] * x_test.transpose()[option]
    plt.plot(x_test.transpose()[option], y, c="blue")
    plt.xlabel(x_legend)
    plt.ylabel(y_legend)

# df = processCSV("car_data.csv")
# train, test = splitTestTrain(df, 0.2)

# x_var, y_var = splitVar(train, ["Age", "Present_Price", "Kms_Driven/100"], ["Selling_Price"])
# x_test, y_test = splitVar(test, ["Age", "Present_Price", "Kms_Driven/100"], ["Selling_Price"])

# coef = calcCoeff(x_var, y_var)

# pred = predict(x_test, coef)

# res = np.c_[y_test, pred]

# r2 = calc_rsquared(y_test, pred)

# print(r2)

# drawReg(x_test, y_test, coef, 1, "Age", "Selling Price")
# plt.show()

# drawReg(x_test, y_test, coef, 2, "Present_Price", "Selling Price")
# plt.show()

# drawReg(x_test, y_test, coef, 3, "Kms_Driven/100", "Selling Price")
# plt.show()

# x_var, y_var = splitVar(train, ["Selling_Price"], ["Present_Price"])

# res = calcCoeff(x_var, y_var)
# print(res)
# print(res.shape)
# print(df.shape[0])
# print(np.ones((301,2)))
# print(np.c_())
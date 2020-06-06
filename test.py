import pandas as pd
from regress import *
from math import *

df = pd.read_csv("data/car data.csv")
n = len(df.index)
n_train = floor(0.8 * n)
n_test = n - n_train

train_data = df[:n_train]
test_data = df[n_train : ]
regression = LinearRegression(train_data)
regression.setDataTest(test_data)
print(regression.sum("Selling_Price"))
regression.setAttribute(["Selling_Price", "Kms_Driven"])
regression.setTarget("Present_Price")
regression.train()
regression.test()
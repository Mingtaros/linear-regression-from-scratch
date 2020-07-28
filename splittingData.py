import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from regression import multipleLinearRegression, koefRegression

data = pd.read_csv('car_dataset.csv', delimiter=",")

# convert to numeric
data[["Year", "Present_Price", "Selling_Price", "Kms_Driven"]] = data[[
    "Year", "Present_Price", "Selling_Price", "Kms_Driven"]].apply(pd.to_numeric)
# insert derived attribut (age)
data.insert(0, "Age", 2020-data[["Year"]])
# insert derived attribut (Kms_Driven/1000)
data.insert(0, "Kms_Driven/2000", data[["Kms_Driven"]]/2000)

y = data[['Selling_Price']]
x = data[['Age', 'Present_Price', 'Kms_Driven/2000']]

# train 80% , test 20% of data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# convert data x dan y menjadi matriks yang bisa diolah
y_train_matrix = y_train.to_numpy(dtype='float')
y_train_matrix = np.reshape(y_train_matrix, (-1, 1))
y_test_matrix = y_test.to_numpy(dtype='float')
x_train_matrix = x_train.to_numpy(dtype='float')
x_test_matrix = x_test.to_numpy(dtype='float')
# add 1 in column 0 buat x_train
x_train_matrix_new = np.insert(x_train_matrix, 0, values=1, axis=1)
x_test_matrix_new = np.insert(x_test_matrix, 0, values=1, axis=1)
print(y_test)
print(x_test)
# data.plot.scatter(x='Kms_Driven', y='Selling_Price', c='DarkBlue')
koef = koefRegression(x_train_matrix_new, y_train_matrix)
print(koef)
print(multipleLinearRegression(
    [x_test_matrix_new[0]], x_train_matrix_new, y_train_matrix))
# print([x_test_matrix_new[3]])
# print(y_test_matrix)
# for i in range(len(x_test_matrix_new)):
#     print(multipleLinearRegression(
#         [x_test_matrix_new[i]], x_train_matrix_new, y_train_matrix))
#     plt.scatter(x_test_matrix[i][0], (multipleLinearRegression(
#         [x_test_matrix_new[i]], x_train_matrix_new, y_train_matrix))[0][0], c="Blue")
# plt.scatter(x_test[['Present_Price']], y_test, c='pink')
# plt.scatter(x_train[['Present_Price']], y_train, c='Pink')
# yval = koef[0][0]+koef[1][0]*x_train[['Year']]+koef[2][0] * \
#     x_train[['Present_Price']]+koef[3][0]*x_train[['Kms_Driven']]
# plt.plot(x_train[['Present_Price']], yval, linestyle='-')
# plt.show()
print(x_test_matrix_new)
for i in range(len(x_test_matrix_new)):
    plt.scatter(x_test_matrix[i][0], (multipleLinearRegression(
        [x_test_matrix_new[i]], x_train_matrix_new, y_train_matrix))[0][0], c="Blue")
plt.scatter(x_test[['Present_Price']], y_test, c='pink')
# plt.scatter(x_train[['Present_Price']], y_train, c='Pink')
yval = koef[0][0]+koef[2][0]*x_train[['Present_Price']]
plt.plot(x_train[['Present_Price']], yval, linestyle='-')
plt.show()

for i in range(len(x_test_matrix_new)):
    plt.scatter(x_test_matrix[i][0], (multipleLinearRegression(
        [x_test_matrix_new[i]], x_train_matrix_new, y_train_matrix))[0][0], c="Blue")
plt.scatter(x_test[['Age']], y_test, c='pink')
yval1 = koef[0][0]+koef[1][0]*x_train[['Age']]
plt.plot(x_train[['Age']], yval1, linestyle='-')
plt.show()

for i in range(len(x_test_matrix_new)):
    plt.scatter(x_test_matrix[i][0], (multipleLinearRegression(
        [x_test_matrix_new[i]], x_train_matrix_new, y_train_matrix))[0][0], c="Blue")
plt.scatter(x_test[['Kms_Driven/2000']], y_test, c='pink')
yval2 = koef[0][0]+koef[3][0]*x_train[['Kms_Driven/2000']]
plt.plot(x_train[['Kms_Driven/2000']], yval2, linestyle='-')
plt.show()

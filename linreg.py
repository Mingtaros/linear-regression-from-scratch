'''
Linear regression module
William Fu - 13518055
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(filename):
    ''' Returns dataframe from a given csv file '''
    return pd.read_csv(filename)

def split_train_test(df, size=0.8, randomize=True):
    ''' Splitting data for train and test '''
    shuffled = None
    # Shuffles the dataframe
    if randomize:
        shuffled = df.sample(frac=1)
    else:
        shuffled = df
    
    # Splits the dataframe to training data and testing data
    train_size = int(size * len(df))
    train = shuffled[:train_size]
    test = shuffled[train_size:]
    
    return train, test

def split_variables(df):
    ''' Splits dataframe into two matrices '''
    rows = df.shape[0]
    ones = np.ones((rows,1))

    x_var = df[['Year', 'Present_Price', 'Kms_Driven']].to_numpy()
    y_var = np.matrix(df['Selling_Price'].to_numpy()).transpose()
    
    return np.c_[ones, x_var], y_var

def calculate_const_coefs(x_var, y_var):
    ''' Calculates the coefficients and constants for
        the regression model '''
    # Transposing X matrices
    xt_var = x_var.transpose()

    # Regression model: Ab = g
    # with A, b, and g are matrices where
    # A = XX', and g = X'y
    a_matrix = np.dot(xt_var, x_var)
    a_matrix_inverse = np.linalg.inv(a_matrix)
    g_matrix = np.dot(xt_var, y_var)

    # List of coeffiecients and constant
    coeffs = np.dot(a_matrix_inverse, g_matrix).transpose()

    return [ coeffs[0,0], coeffs[0,1], coeffs[0,2], coeffs[0,3] ]

def predict(x_var, coeffs):
    ''' Returns a list filled with predicted values '''
    predicted_values = []

    for i in range(x_var.shape[0]):
        value = coeffs[0]
        for j in range(1, x_var.shape[1]):
            value += coeffs[j]*x_var[i,j]
        predicted_values.append(value)
    
    return predicted_values

def calculate_error(actual, predicted):
    ''' Returns a list filled with errors 
    (actual value - predicted values) '''
    return [ actual[i] - predicted[i] for i in range(len(predicted))]

def calculate_deviation(actual):
    ''' Returns a list filled with deviations between
    predictions and average actual values '''
    y_mean = np.sum(actual) / len(actual)
    return [ value - y_mean for value in actual ]

def calculate_sse(errors):
    ''' Calculates SSE '''
    return np.sum([error**2 for error in errors])

def calculate_sst(deviations):
    ''' Calculates SST '''
    return np.sum([deviation**2 for deviation in deviations])

def calculate_rsquared(actual, predicted):
    ''' Calculates R-Squared '''
    # Calculating SSE dan SST values
    errors = calculate_error(actual, predicted)
    deviations = calculate_deviation(actual)
    sse, sst = calculate_sse(errors), calculate_sst(deviations)
    
    # Outputs
    print("SSE = {:.4f}".format(sse))
    print("SST = {:.4f}".format(sst))
    return 1 - (sse/sst)

def draw_regression(x_axis, y_axis, coeffs, item, legend):
    ''' Draws a regression line '''
    min_x = np.min(x_axis[item])
    max_x = np.max(x_axis[item])
    x = np.linspace(min_x, max_x, 10)
    y = coeffs[0 if item == 1 else 1] * np.ones(len(x)) + coeffs[item] * x
    
    plt.plot(x, y, c='red')
    plt.scatter(x_axis[item], y_axis)
    plt.title(legend)
    plt.xlabel(legend)
    plt.ylabel('Selling_Price')   

if __name__ == "__main__":

    df = pd.read_csv("car_data.csv")[['Year','Present_Price', 'Kms_Driven', 'Selling_Price']]
    train, test = split_train_test(df)
    x_var, y_var = split_variables(train)
    x_test, y_test = split_variables(test)
    coeffs = calculate_const_coefs(x_var, y_var)
    predicted = predict(x_test, coeffs)
    rsq = calculate_rsquared(y_test, predicted)

    x_axis = x_test.transpose()
    y_axis = np.array(y_test.transpose()).flatten()
    
    draw_regression(x_axis, y_axis, coeffs, 3, "Kms_Driven")
    plt.show()
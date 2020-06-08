# Linear Regression from Scratch
Linear Regression Module from 0 using julia and implemented in julia.ipynb

## Source Code
The source code consists of a module in julia and an ipynb file for implementation. <br>
In the module I used LinearAlgebra, Statistics, and DataFrames packages from julia to compute some calculation and to load the data itself. In the implementation I added Plots to show the visualization and CSV to read the csv given. <br>
### Module
#### Constructor
The algorithm module's constructor has attributes such as    <br>
    - dataset: the data <br>
    - xvar: the independent variables that affect the y variable <br>
    - yvar: the variable affected <br>
    - coeff: array of coeffisiens <br>
#### Functions
and functions such as <br>
##### linearRegression 
    ```
    input: self
    return: array of coeff
    ```
  
    This function performs the calculation to find the array of coefficient by creating 
    an array consisting the dot products of x variables and y variable and matrix of x, 
    thus multiplying the invers of x matrix with the array.
    
##### Prediction
    ```
    input: self, data_test
    output: array of predictions
    ```
    
    This function performs the calculation of prediction array by appending the array in 
    question with the multiplication of array of coefficients with the testing data. 
    
##### Error Parameter 
    ```
    input: self, predictions, data_test 
    output: rms and mean abs error
    ```
    This function will return the mean absolute error and the root mean square error by
    processing the difference between the result of prediction and the actual data

## Theory
Multiple linear regression is a statistical technique that uses several explanatory variables to predict the outcome of a response variable. The goal of multiple linear regression (MLR) is to model the linear relationship between the explanatory (independent) variables and response (dependent) variable. <br>
A multiple linear regression model with k predictor variables X1, X2, ..., Xk
and a response Y , can be written as <br>
y = β0 + β1x1 + ··· + βkxk + e <br>
with B as regression coefficients and e as the residual terms.
The observations can be seen as points in (k + 1)-dimensional space.
The goal in least-squares regression is to fit a hyper-plane into (k + 1)-dimensional space that minimizes the sum of squared residuals.
The derivation could be taken to the model parameters β0,..., βk, set them equal to zero and derive the least-squares normal equations that our parameter estimates β0,..., βk would have to fulfill.
These equations are much more conveniently formulated with the help of vectors
and matrices. <br>
Say we have an array of y, matrix of x, array of coefficients, and array of residual. In tsuch notation, y can be obtained by multiplying the matrix x with array of coefficients and add the array of residual to have array of y. <br>
In linear algebra terms, the least-squares parameter estimates β are the vectors that minimize the residual function. 
The vector normal equations are the same normal equations that one could obtain
from taking derivatives. To solve the normal equations (i.e., to find the parameter
estimates βˆ), one can multiply both sides with the inverse of X'X. Thus, the least-squares estimator of β is (in vector form)

## Requirement
1. Jupyter Notebook
2. Julia
3. From Julia: CSV, DataFrames, LinearAlgebra, Statistics, Plots

## Reference
### Julia
Language: <br>
https://docs.julialang.org/<br>
https://cheatsheets.quantecon.org/julia-cheatsheet.html<br>
https://datatofish.com/julia-tutorials/
<br>
Calculation: <br>
https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/<br>
https://docs.julialang.org/en/v1/stdlib/Statistics/<br>
<br>
Plotting: <br>
https://docs.juliaplots.org/latest/tutorial/
<br>

### Linear Regression
Algorithm: <br>
http://www.stat.yale.edu/Courses/1997-98/101/linmult.htm<br>
https://towardsdatascience.com/julia-for-data-science-how-to-build-linear-regression-from-scratch-with-julia-6d1521a00611<br>
https://alexandrugris.github.io/machine/learning/2017/03/25/MachineLearning-Notebook-2.html
<br>
Splitting: <br>
https://developers.google.com/machine-learning/crash-course/training-and-test-sets/splitting-data

## Author
Byan Sakura
13518066

# Linear Regression from Scratch
Linear Regression Module from 0 using julia and implemented in julia.ipynb

## Source Code
The source code consists of a module in julia and an ipynb file for implementation. 
In the module I used LinearAlgebra, Statistics, and DataFrames packages from julia to compute some calculation and to load the data itself. In the implementation I added Plots to show the visualization and CSV to read the csv given.
The algorithm module's constructor has attributes such as    <br>
    dataset: the data <br>
    xvar: the independent variables that affect the y variable <br>
    yvar: the variable affected <br>
    coeff: array of coeffisiens <br>
and functions such as <br>
    linearRegression
    ```
    input: self
    return: array of coeff
    ```
    Prediction
    ```
    input: self, data_test
    output: array of predictions
    ```
    Error Parameter
    ```
    input: self, predictions, data_test
    output: rms and mean abs error
    ```

## Theory
Linear regression is a statistical approach for modelling relationship between a dependent variable with a given set of independent variables.

## Reference
### Julia
Language: <br>
https://docs.julialang.org/
https://cheatsheets.quantecon.org/julia-cheatsheet.html
https://datatofish.com/julia-tutorials/
<br>
Calculation: <br>
https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/
https://docs.julialang.org/en/v1/stdlib/Statistics/
<br>
Plotting: <br>
https://docs.juliaplots.org/latest/tutorial/
<br>

### Linear Regression
Algorithm: <br>
http://www.stat.yale.edu/Courses/1997-98/101/linmult.htm
https://towardsdatascience.com/julia-for-data-science-how-to-build-linear-regression-from-scratch-with-julia-6d1521a00611
https://alexandrugris.github.io/machine/learning/2017/03/25/MachineLearning-Notebook-2.html
<br>
Splitting: <br>
https://developers.google.com/machine-learning/crash-course/training-and-test-sets/splitting-data

## Author
Byan Sakura
13518066

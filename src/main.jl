include("regression.jl")
using .LinearRegression

matX = [[0, 10, 20, 30, 40]]
arrY = [[31, 32, 47, 79, 89]]


N = length(arrY[1])
k = length(matX)

Reg = LinearRegression.Regression(matX, arrY, [], N, k)

LinearRegression.run(Reg)
LinearRegression.test(Reg, matX, arrY)
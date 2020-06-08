include("loader.jl")
include("regression.jl")
using .DataLoader
using .LinearRegression

L = DataLoader.Loader("car_data.csv", 0.8, [], [], [], 0, [], [])
DataLoader.loader_run(L)

XTrain = [[0, 10, 20, 30, 40]]
YTrain = [[31, 32, 47, 79, 89]]
XTest = DataLoader.get_X_test(L)
YTest = DataLoader.get_Y_test(L)
println("XTrain: ")
println(XTrain)
println("YTrain: ")
println(YTrain)
# println("XTest: ")
# println(XTest)
# println("YTest: ")
# println(YTest)

N = length(XTrain[1])
k = length(YTrain)

Reg = LinearRegression.Regression(XTrain, YTrain, [], N, k)

LinearRegression.run(Reg)
# LinearRegression.test(Reg, XTest, YTest)
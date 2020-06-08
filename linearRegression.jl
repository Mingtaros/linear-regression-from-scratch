module linearRegression

using LinearAlgebra, Statistics, DataFrames

#Construction
#= Structing linReg that consists of dataset, xvar, yvar, coeff=#
mutable struct linReg
    dataset
    xvar
    yvar
    coeff
end

#linearRegression
#= 
input: self
return: array of coeff
=#
function lin(l::linReg)
    n = size(l.xvar,1)
    arrY = zeros(n+1)
    arrY[1] = sum(l.dataset[:,l.yvar])
    for i = 1 : n
        arrY[i+1]=dot(l.dataset[:,l.xvar[i]], l.dataset[:,l.yvar])
    end

    arr = zeros(n+1, n+1)
    for i=1 : n+1
        for j=1 : n+1
            if i==1
                if j==1 
                    arr[i,j]=size(l.dataset,1) else arr[i,j]= sum(l.dataset[:,l.xvar[j-1]])
                end
            else
                if j==1
                    arr[i,j]=sum(l.dataset[:,l.xvar[i-1]]) else arr[i,j]= dot(l.dataset[:,l.xvar[i-1]],l.dataset[:,l.xvar[j-1]])
                end
            end
        end
    end
    l.coeff= inv(arr)*arrY
end

#Prediction
#=
input: self, data_test
output: array of predictions
=#
function prediction(l::linReg, testing)
    n = nrow(testing)
    result = zeros(n)

    for i = 1 : size(l.coeff, 1)
        for j = 1 : n 
            if i == 1
                result[j] = l.coeff[i]
            else
                result[j] += l.coeff[i] * testing[j:j,l.xvar[i-1]][1]
            end
        end
    end
    return result
end

#=Error Parameter
input: self, predictions, data_test
output: rms and mean abs error
=#
function errMeter(l::linReg, result, testing)
    n = nrow(testing)
    means = 0
    actY = testing[:,l.yvar]
    for i = 1 : n
        means += abs(result[i] - actY[i])
    end

    Rmse = 0
    for i = 1 : n
        errorRmse = (result[i] - actY[i])^2
        Rmse += errorRmse
    end

    rmse = (Rmse / n)^0.5
    mar = means / n
    println("Mean absolute error : $(mar)")
    println("Root mean square error : $(rmse)")
end

end




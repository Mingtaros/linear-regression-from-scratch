module LinearRegression

using LinearAlgebra, Compat, Statistics, DataFrames

mutable struct Regression
    data
    attribute
    target
    model
    dataTest
end

function setData(r::Regression, dataInput)
    r.data = dataInput
    return nothing
end

function setAttribute(r::Regression, attribute)
    r.attribute = attribute
    return nothing
end

function setTarget(r::Regression, target)
    r.target = target
    return nothing
end

function setDataTest(r::Regression, dataTest)
    r.dataTest = dataTest
    return nothing
end

function sumByAttribute(r::Regression, attribute)
    return sum(r.data[:,attribute])
end

function sumProd(r::Regression, A, B)
    dataA = r.data[:,A]
    dataB = r.data[:,B]
    return dot(dataA, dataB)
end

function train(r::Regression)
    n = size(r.attribute, 1)
    tmpTarget = zeros(n+1)
    tmpTarget[1] = sumByAttribute(r, r.target)
    for i = 1 : n
        tmpTarget[i+1] = sumProd(r, r.attribute[i], r.target)
    end

    n_data = size(r.data,1)
    tmp = zeros(n+1, n+1)
    for i = 1 : n+1
        for j = 1 : n+1
            if i == 1
                if j == 1
                    tmp[i,j] = n_data
                else
                    tmp[i,j] = sumByAttribute(r, r.attribute[j-1])
                end
            else
                if j == 1
                    tmp[i,j] = sumByAttribute(r, r.attribute[i-1])
                else
                    tmp[i,j] = sumProd(r, r.attribute[i-1], r.attribute[j-1])
                end
            end
        end
    end

    r.model = inv(tmp)*tmpTarget
end

function predict(r::Regression)
    n = nrow(r.dataTest)
    result = zeros(n)

    for i = 1 : size(r.model, 1)
        for j = 1 : n 
            if i == 1
                result[j] = r.model[i]
            else
                result[j] += r.model[i] * r.dataTest[j:j,r.attribute[i-1]][1]
            end
        end
    end

    sum = 0
    targetValue = r.dataTest[:,r.target]
    for i = 1 : n
        error = abs(result[i] - targetValue[i])
        sum += error
    end

    sumRmse = 0
    for i = 1 : n
        errorRmse = (result[i] - targetValue[i])^2
        sumRmse += errorRmse
    end

    rmse = (sumRmse / n)^0.5


    mean_absolute_error = sum / n
    println("Mean absolute error : $(mean_absolute_error)")
    println("Root mean square error : $(rmse)")
    return result
end

end
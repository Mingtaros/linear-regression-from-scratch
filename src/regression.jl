# regression.jl
# Contain all module to process certain data to get the regression linear
module LinearRegression

mutable struct Regression
    matX
    matY
    matB
    N
    k
end

# Set all x-atribute data into matX
function set_matX(reg::Regression, matX)
    reg.matX = matX
    return nothing
end

# Set k-value to determine how many x-variable it is
function set_k(reg::Regression, k)
    reg.k = k
    return nothing
end

# Set n-value to determine how many data it is
function set_N(reg::Regression, N)
    reg.N = N
    return nothing
end

# Square a value
function sqr(val)
    return val * val
end

# Show regression equation
function showRegression(reg::Regression, l)
    rest = ""
    for i = 2:reg.k+1
        if (reg.matB[l][i] >= 0)
            rest = rest * " + " * string(reg.matB[l][i]) * "x" * string(i-1)
        else
            rest = rest * " - " * string(-reg.matB[l][i]) * "x" * string(i-1)
        end
    end
    result = "y_hat = " * string(reg.matB[l][1]) * rest
    println(result)
    return nothing
end

# Compute the predicted value Y based on regression equation
function regression_Value(reg::Regression, P, l)
    sum = 0
    for i = 2:reg.k+1
        sum = sum + reg.matB[l][i] * P[i-1]
    end
    return reg.matB[l][1] + sum
end

# Compute Y Hat value for each X Test value
function compute_YHat(reg::Regression, testX, numOfData, l)
    testYHat = []
    for i = 1:numOfData
        P = []
        for j = 2:reg.k+1
            append!(P, [testX[j-1][i]])
        end
        append!(testYHat, [regression_Value(reg, P, l)])
    end
    return testYHat
end

# Sum all value of array arr
function sum_Array_Data(arr)
    sum = 0
    i = 0
    n = length(arr)
    for i = 1:n
        sum = sum + arr[i]
    end
    return sum
end

# Sum all multiplied of array A and array B
function sum_Multiply_Data(A, B)
    sum = 0
    i = 0
    n = length(A)
    for i = 1:n
        sum = sum + A[i] * B[i]
    end
    return sum
end

# Generate all linear equation
function generate_Linear_Equation(reg::Regression, arrY)
    Matrix = []
    # Compute left-value
    for i = 1:reg.k+1
        Row = []
        for j = 1:reg.k+1
            result = 0
            if ((i == 1) && (j == 1))
                result = reg.N
            elseif (i == 1)
                result = sum_Array_Data(reg.matX[j-1])
            elseif (j == 1)
                result = sum_Array_Data(reg.matX[i-1])
            else
                result = sum_Multiply_Data(reg.matX[i-1], reg.matX[j-1])
            end
            append!(Row, [result])
        end
        append!(Matrix, [Row])
    end

    # Compute right-value
    for i = 1:reg.k+1
        if (i == 1)
            result = sum_Array_Data(arrY)
        else
            result = sum_Multiply_Data(reg.matX[i-1], arrY)
        end
        append!(Matrix[i], [result])
    end
    return Matrix
end

# Compute all linear equation to get b0, b1, ..., bN
function solve_Equation(reg::Regression, M)
    n = reg.k + 1
    for j = 1:n
        for i = 1:n
            if (i != j)
                c = M[i][j] / M[j][j]
                for k = 1:n+1
                    M[i][k] = M[i][k] - (c * M[j][k])
                end
            end
        end
    end

    b = []
    for i = 1:n
        val = M[i][n+1] / M[i][i]
        append!(b, [val])
    end
    append!(reg.matB, [b])
    return nothing
end

# Return the mean of all data
function mean(arr)
    sum = 0
    i = 0
    n = length(arr)
    for i = 1:n
        sum = sum + arr[i]
    end
    return sum / n
end

# Compute least square estimation  or sum square of error (SSE)
function compute_SSE(realY, hatY)
    sum = 0
    i = 0
    n = length(realY)
    for i = 1:n
        sum = sum + sqr(realY[i] - hatY[i])
    end
    return sum
end
    
# Compute sum square of total
function compute_SST(realY)
    sum = 0
    i = 0
    y_mean = mean(realY)
    n = length(realY)
    for i = 1:n
        sum = sum + sqr(realY[i] - y_mean)
    end
    return sum
end

# Compute the coefficient of determination
function compute_RSquare(realY, hatY)
    SSE = compute_SSE(realY, hatY)
    SST = compute_SST(realY)
    return 1 - (SSE / SST)
end

# Process all arrX and arrY data to get regression linear equation
function run(reg::Regression)
    println("success")
    for i = 1:length(reg.matY)
        Matrix = generate_Linear_Equation(reg, reg.matY[i])
        solve_Equation(reg, Matrix)
        showRegression(reg, i)
    end
    return nothing
end

# Test the regression with test dataset
function test(reg::Regression, testFrame, testY)
    numOfData = length(testFrame[1])
    for l = 1:length(testY)
        YHat = compute_YHat(reg, testFrame, numOfData, l)
        print("#\t\t")
        for i = 1:length(testFrame)
            printed = "X" * string(i) * "\t\t"
            print(printed)
        end
        println("Y\t\t YHat")
        for i = 1:numOfData
            result = string(i) * "\t\t"
            for j = 1:length(testFrame)
                result = result * string(testFrame[j][i]) * "\t\t"
            end
            result = result * string(testY[l][i]) * "\t\t"
            result = result * string(YHat[i])
            println(result)
        end
        println("Regression Accuracy = ",compute_RSquare(testY[l], YHat))
    end
end

end
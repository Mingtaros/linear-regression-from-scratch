module linearRegression

mutable struct regression
    xdata
    ydata
    num_data
    num_free_var
    xmatrix
    bmatrix
    ymatrix
end

# Fungsi untuk memasukkan data x dari dataframe ke dalam matrix
function put_into_xmatrix(reg::regression, data, row)
    x_temp = Matrix{Float64}(undef, row, reg.num_free_var+1)
    for i = 1:(row)
        for j = 1:(reg.num_free_var+1)
            if(j == 1)
                x_temp[i,j] = 1.00
            else
                x_temp[i,j] = data[i, j-1]
            end
        end
    end

    return x_temp
end

# Fungsi untuk memasukkan data y dari dataframe ke dalam matrix
function put_into_ymatrix(reg::regression, data, row)
    y_temp = Matrix{Float64}(undef, row, 1)
    for i = 1:(row)
        y_temp[i,1] = data[i, 1]
    end

    return y_temp
end

# Prosedur untuk melakukan perhitungan nilai b
function calculate_B(reg::regression)
    temp1 = transpose(reg.xmatrix) * reg.xmatrix
    temp2 = transpose(reg.xmatrix) * reg.ymatrix
    reg.bmatrix = inv(temp1) * transpose(reg.xmatrix) * reg.ymatrix

    return nothing

end

# prosedur untuk mencetak persamaan hasil regresi ke layar
function print_equation(reg::regression)
    equation = "ŷ = " * string(reg.bmatrix[1,1]) * " "
    temp = ""
    for i = 2:(reg.num_free_var+1)
        if(reg.bmatrix[i,1] >= 0)
            temp = temp * "+" * string(reg.bmatrix[i,1]) * "x" * string(i-1) * " "
        else
            temp = temp * string(reg.bmatrix[i,1]) * "x" * string(i-1) * " "
        end
    end
    equation = equation * temp
    println("The fitted regression model:")
    println(equation)

    return nothing
end

# fungsi untuk menghitung rata-rata nilai y pada array arr
function y_means(reg::regression, arr, n_row)
    sum = 0
    for i=1:n_row
        sum = sum + arr[i,1]
    end
    return sum/n_row  
end

# fungsi untuk menghitung hasil penjumlahan seluruh element array yang dikuadratkan
function sum_prod(reg::regression, arr)
    sum = 0
    for i = 1:length(arr)
        sum = sum + (arr[i] * arr[i])
    end
    return sum
end

# fungsi untuk menghitung nilai MSE
function calculate_MSE(reg::regression, arr)
    return (1/length(arr)) * sum_prod(reg,arr)
end

# fungsi untuk menghitung nilai RMSE
function calculate_RMSE(reg::regression, mse)
    return sqrt(mse)
end

# fungsi untuk menghitung nilai RSquare
function calculate_RSquare(reg::regression, arr1, arr_test_y, n_row)
    ymean = y_means(reg,arr_test_y,n_row)
    arr2 = []
    for i=1:n_row
        append!(arr2, arr_test_y[i,1]-ymean)
    end

    temp = sum_prod(reg, arr1)/sum_prod(reg,arr2)
    return (1-temp)
end

# fungsi yang melakukan train terhadap data untuk menghasilkan persamaan regresi linear
function train(reg::regression)
    reg.xmatrix = put_into_xmatrix(reg, reg.xdata, reg.num_data)
    reg.ymatrix = put_into_ymatrix(reg, reg.ydata, reg.num_data)

    calculate_B(reg)
    print_equation(reg)
    return reg.bmatrix
end


# fungsi yang melakukan prediksi terhadap data test dan menampilkan akurasi perhtingan
function test(reg::regression, x_test, y_test, n_row_test)
    println("x1\t\tx2\t\tx3\t\ty\t\tŷ\t\ty-ŷ")

    xtest_matrix = put_into_xmatrix(reg, x_test, n_row_test)
    ytest_matrix = put_into_ymatrix(reg, y_test, n_row_test)

    arr_predicted_y = []
    y_min_ypredicted = []
    for i=1:n_row_test
        temp = ""
        predicted_y = reg.bmatrix[1,1]
        for j = 2:reg.num_free_var+1
            predicted_y = predicted_y + xtest_matrix[i,j] * reg.bmatrix[j,1]
            temp = temp * string(round(xtest_matrix[i,j], digits=5))
            if(length(string(xtest_matrix[i,j]))>=8)
                temp = temp * "\t"
            else
                temp = temp * "\t\t"
            end
        end
        temp = temp * string(round(ytest_matrix[i,1],digits=5)) * "\t\t"
        append!(arr_predicted_y, predicted_y)
        append!(y_min_ypredicted, ytest_matrix[i,1]-predicted_y)

        temp = temp * string(round(predicted_y, digits=5))
        if(length(string(round(predicted_y, digits=5)))>=8)
            temp = temp * "\t"
        else
            temp = temp * "\t\t"
        end

        temp = temp * string(round(ytest_matrix[i,1]-predicted_y, digits=5))
        println(temp)
    end

       # Menghitung akurasi
    MSE = calculate_MSE(reg, y_min_ypredicted)
    RMSE = calculate_RMSE(reg, MSE)
    RSquare = calculate_RSquare(reg, y_min_ypredicted, y_test, n_row_test)
    println("Mean Square Error = " * string(MSE))
    println("Root Mean Square Error = " * string(RMSE))
    println("Root Square = " * string(RSquare))
    return convert(Array{Float64,1}, arr_predicted_y)


end


end

module regression

export multipleLinearRegression
function multipleLinearRegression(xPredict, x, y)
    # mengembalikan hasil prediksi dari inputan data x
    # xPredict=[1,x1,x2,x3,..]
    return(xPredict*koefRegression(x, y))
end

function koefRegression(x, y)
    # mengembalikan array of koefisien (B)
    # x merupakan matriks nx(p+1), dimana p adalah jumlah var bebas (independent variables)
    # y merupakan matriks nx1
    # B = (invers(X'X))*(X'Y)
    xTrans = transpose(x)
    inverse = inv(xTrans*x)
    xTransy = xTrans*y
    B = inverse*xTransy
    return B
end


end # module
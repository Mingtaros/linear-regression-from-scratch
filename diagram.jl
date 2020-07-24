module Diagram

using Plots

    function Visualize(col_inp, data_test, n, n_train, result)
        factor1=ones(n - Int(floor(n * 0.8)))
        col = data_test[:, col_inp]
        yp = [factor1 col]
        coCol = yp\result
        f1 = coCol[1]*factor1 + coCol[2]*col
        diagramTitle = col_inp * " vs Present Price"

        p1=scatter(col,result, color=:blue, label= "Predicted Data")
        p1=plot!(col,f1,linewidth=1, color=:red,label = "Prediction", title=diagramTitle)

        plot(p1)
    end

end
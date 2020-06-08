# export linreg
using LinearAlgebra

module LinReg

    export linreg, dotproduct, train

    mutable struct linreg
        weight:: Array{Float64,2}
        bias:: Array{Float64,2}
        learnrate::Float64
        function linreg(xnum::Integer,ydim::Integer,learnrate::Float64)
            # x = new()
            weight = zeros(Float64,ydim,xnum)
            bias = zeros(Float64,1,ydim)
            learnrate = learnrate
            new(weight,bias,learnrate)
        end
    end

    function dotproduct(a :: Array{Float64,2}, b :: Array{Float64,2})
        x = size(a,1)
        y = size(b,2)
        # hasil = Array{Float64,2}(undef,x,y)
        hasil = zeros(Float64,x,y)
        for i in 1:x
            for j in 1:y
                for k in 1:size(a,2)
                    hasil[i,j] += a[i,k] * b[k,j] 
                end
            end
        end
        return hasil
    end

    function train(model::linreg, data::Array{Float64,2}, iter::Integer)
        features = data[:,1:size(data,2)-1]
        labels = data[:,size(data,2)]
        # show(features[1,:])
        # show(labels)
        for _ in 1:iter
            for i in 1:size(features,1)
                hypothesis = model.bias .+ dot(model.weight,features[i,:])
                #============ Explanation =========
                y^ is hypothesis (label), y is for the real value (label)
                every iteratiorn, the weight will be updated
                weight will be updated by dLoss/dweight, where Loss is calculated using 
                    Mean Squared Error = (1/N sigma (i : [1..n] (yi - y^i) ** 2))
                        Where N is the output vector length, in cases where Y is single valued it is a normal float
                dL/dw = dL/d y^ * d y^/dw 
                    where dL/dy^ = dL/d(y - y^) * d(y-y^)/dy^
                    where d(y-y^)/dy^ = -1 and dL/d(y -y^) = 2 * (y-y^), therefore dL/dy^ = -2 * (y - y^)
                    since y^  = features . weight + bias , therefore dy^/dw = features
                therefore dL/dw = -2 * (y - y^) * features
                new weight = old weight - learnrate * dL/dw =#
                model.weight = model.weight - ((model.learnrate / size(model.weight,1) * -2) .* dotproduct((labels[i:i,:] - hypothesis),features[i:i,:]))
                model.bias = model.bias - ((model.learnrate * -2)*(labels[i:i,] - hypothesis))
            end
        end
    end

end

a = linreg(3,1,0.005)
data = zeros(Float64,5,4)
for i in 1:size(data,1)
    tot = 0
    for j in 1:size(data,2)
        if j != size(data,2)
            data[i,j] = sqrt(((rand(Int)%8))^2)+1
            tot = tot + data[i,j] * j
        else
            data[i,j] = tot
        end
    end
end
# train(a,data,3000)
# show(a.weight)
# visualizer.jl
# Module to visualize the map and the streets in complex way
# The visualization is using Plots library

module Visualizer

using Plots

function Visualize(XTest, YTest, B0, B1, XLabel, YLabel)
    plotTitle = XLabel * " dan " * YLabel
    scatter(XTest, YTest, title = plotTitle, label="Data test")
    xiter = minimum(XTest):maximum(XTest)
    yiter = []
    for x in xiter
        value = B0 + B1 * x
        append!(yiter, [value])
    end
    xlabel!(XLabel, fontsize = 20)
    ylabel!(YLabel, fontsize = 20)
    return plot!(xiter, yiter, color=:red, label="Regresi")
end

end
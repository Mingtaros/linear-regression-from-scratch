# loader.jl
# Load .csv data to program variables
module DataLoader

using CSV
using DataFrames

mutable struct Loader
    fileName
    splitFactor
    dataFrame
    trainFrame
    testFrame
    midpoint
    x_columns
    y_columns
end

# Split dataframe into trainFrame and testFrame
function split_dataFrame(ldr::Loader)
    size = nrow(ldr.dataFrame)
    ldr.midpoint = convert(Int64, round(size * ldr.splitFactor, digits=0))
    ldr.trainFrame = ldr.dataFrame[1: ldr.midpoint,:]
    ldr.testFrame = ldr.dataFrame[ldr.midpoint: size,:]
    println("Train Dataframe")
    println(ldr.trainFrame)
    println()
    println("Test Dataframe")
    println(ldr.testFrame)
    return nothing
end

# Get column index based on column name
function get_column_index(ldr::Loader, listName)
    result = []
    cols = propertynames(ldr.dataFrame)
    for i = 1:length(listName)
        for j = 1:length(cols)
            if (listName[i] == string(cols[j]))
                append!(result, [j])
            end
        end
    end
    return result
end

# Get all column of the dataframe
function get_All_Column(ldr::Loader)
    result = []
    cols = propertynames(ldr.dataFrame)
    for i = 1:length(cols)
        append!(result, [string(cols[i])])
    end
    return result
end

# Get numeric columns of the dataFrame
function get_Numeric_Columns(ldr::Loader)
    result = []
    cols = propertynames(ldr.dataFrame)
    for i = 1:length(cols)
        if ((eltype(ldr.dataFrame[1,i]) == Int64) ||(eltype(ldr.dataFrame[1,i]) == Float64))
            append!(result, [string(cols[i])])
        end
    end
    return result
end

# Get all train x_columns dataset value
function get_X_train(ldr::Loader)
    matX = []
    idx = get_column_index(ldr, ldr.x_columns)
    for i = 1:length(ldr.x_columns)
        arrX = []
        for j = 1:nrow(ldr.trainFrame)
            append!(arrX, [ldr.trainFrame[j, idx[i]]])
        end
        append!(matX, [arrX])
    end
    return matX
end

# Get all train y_columns dataset value
function get_Y_train(ldr::Loader)
    matY = []
    idx = get_column_index(ldr, ldr.y_columns)
    for i = 1:length(ldr.y_columns)
        arrY = []
        for j = 1:nrow(ldr.trainFrame)
            append!(arrY, [ldr.trainFrame[j, idx[i]]])
        end
        append!(matY, [arrY])
    end
    return matY
end

# Get all test x_columns dataset value
function get_X_test(ldr::Loader)
    matX = []
    idx = get_column_index(ldr, ldr.x_columns)
    for i = 1:length(ldr.x_columns)
        arrX = []
        for j = 1:nrow(ldr.testFrame)
            append!(arrX, [ldr.testFrame[j, idx[i]]])
        end
        append!(matX, [arrX])
    end
    return matX
end

# Get all test y_columns dataset value
function get_Y_test(ldr::Loader)
    matY = []
    idx = get_column_index(ldr, ldr.y_columns)
    for i = 1:length(ldr.y_columns)
        arrY = []
        for j = 1:nrow(ldr.testFrame)
            append!(arrY, [ldr.testFrame[j, idx[i]]])
        end
        append!(matY, [arrY])
    end
    return matY
end

# Get x-column i name
function get_x_column(ldr::Loader, i)
    return ldr.x_columns[i]
end

# Get y-column i name
function get_y_column(ldr::Loader, i)
    return ldr.y_columns[i]
end

# Execute loader
function loader_run(ldr::Loader)
    ldr.dataFrame = CSV.read("../data/UAS_2019.csv")
    split_dataFrame(ldr::Loader)

    all_cols = get_All_Column(ldr)
    println("All column: ")
    for i = 1:length(all_cols)
        println(string(i) * ". " * all_cols[i])
    end
    println()

    num_cols = get_Numeric_Columns(ldr)
    println("Numeric columns: ")
    for i = 1:length(num_cols)
        println(string(i) * ". " * num_cols[i])
    end
    println()
    ldr.x_columns = ["waktu_berangkat"]
    ldr.y_columns = ["waktu_tempuh"]
    println("Selected x variable: ")
    for i = 1:length(ldr.x_columns)
        println(string(i) * ". " * ldr.x_columns[i])
    end
    println()
    println("Selected y variable: ")
    for i = 1:length(ldr.y_columns)
        println(string(i) * ". " * ldr.y_columns[i])
    end
end

end
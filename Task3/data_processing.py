import numpy as np
def matrix_conversion(file_name):
    data_array = []
    file_handle = open("database,matrix/"+file_name)
    for i in file_handle:
        x = i.strip().split(",")
        for j in x:
            data_array.append(j)

    new_data_array = []
    for i in data_array:
        try:
            x = int(i)
            new_data_array.append(x)
        except:
            continue
        else:
            continue
    file_handle.close()
    height = new_data_array.pop()
    width = new_data_array.pop()
    size = (width,height)
    data = []
    pesudo_data = []
    for y in range(height):
        data.append(pesudo_data[::-1])
        for x in range(width):
            pesudo_data.append(new_data_array.pop())
    data = data[::-1]
    return data,size

array,size = matrix_conversion("face1.txt")
print(array[1])
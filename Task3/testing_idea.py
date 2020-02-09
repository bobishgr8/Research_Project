from PIL import Image
import random
def file_reader(file_name):
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
    return new_data_array,size
        


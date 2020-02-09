#this file tries the idea of a threshold value
from PIL import Image
import numpy as np
from statistics import median 

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




face1,face1_size = file_reader("face1.txt")

unknown,unknown_size = file_reader("face1-A.txt")



face1_data_arr = [face1,face1_size]

unknown_data_arr = [unknown,unknown_size]

def mean_extract(array):
    features = []  #mean
    features.append(max(array[0])/len(array[0])) #gets mean
    copy_of_face1 = array[0][:]
    features.append(median(sorted(copy_of_face1)))
    return features


np_arr = np.array(face1).reshape((207,-1))
print(np.linalg.eigvals(np_arr))
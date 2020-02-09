import numpy as np
import statistics

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

def mean_per_row(array,height):
    mean_per_row = []
    data = np.array(array).reshape(height,-1)
    for i in data:
        mean_per_row.append(sum(i)/len(i))
    return mean_per_row

def median_per_row(array,height):
    median_per_row = []
    data = np.array(array).reshape(height,-1)
    for i in data:
        median_per_row.append(statistics.median(i))
    return median_per_row

mean_val = []
median_val = []
for i in range(1,6):
    holder,size = file_reader("face"+str(i)+".txt")
    holder_mean_per_row = mean_per_row(holder,size[1])
    holder_median_per_row = median_per_row(holder,size[1])
    mean_val.append(holder_mean_per_row)
    median_val.append(holder_median_per_row)

print("\n")

unknown,size = file_reader("face1.txt")
unknown_mean_per_row = mean_per_row(unknown,size[1])
unknown_median_per_row = median_per_row(unknown,size[1])

unknown2,size2 = file_reader("face1-A.txt")
unknown_mean_per_row2 = mean_per_row(unknown2,size2[1])
unknown_median_per_row2 = median_per_row(unknown2,size2[1])

def confidence_rank(unknown_mean,unknown_median):
    print("the sum for this unknown's mean: ")
    sum_val = 0
    count = 1
    for array in mean_val:
        for j in range(len(unknown_mean)):
            sum_val += array[j]-unknown_mean[j]
        sum_val = sum_val/len(unknown_mean)
        print("sum for the "+str(count)+" image is: "+str(sum_val.__abs__()))
        count+=1
        sum_val = 0
    print("the sum for this unknown's median: ")
    sum_val = 0
    count = 1
    for array in median_val:
        for j in range(len(unknown_median)):
            sum_val += array[j]-unknown_median[j]
        sum_val = sum_val/len(unknown_median)
        print("sum for the "+str(count)+" image is: "+str(sum_val.__abs__()))
        count+=1
        sum_val = 0

            

confidence_rank(unknown_mean_per_row,unknown_median_per_row)
print("\n")
confidence_rank(unknown_mean_per_row2,unknown_median_per_row2)
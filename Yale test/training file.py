import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import random

data_plot = []

def file_reader(file_name):
    data_array = []
    file_handle = open(file_name)
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
# configure this array's length to determine the test to training ratio

file_names_in_test_set = ["centerlight","glasses"]
#,"happy", "leftlight", "noglasses", "normal", "rightlight", "sad", "sleepy", "wink"]

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    for j in file_names_in_test_set:
        try:
            vector,size = file_reader(f"yalefaces/subject{no_var}.{str(j)}.txt")
            data_plot.append(vector)
        except:
            print("Exception1")
            continue
        

def distance(arr1,arr2):
    if len(arr1) != len(arr2):
        return Exception
    distance = 0
    diff = []
    for i in range(len(arr2)-1):
        diff.append((int(arr2[i])-int(arr1[i]))**2)
    distance = sum(diff)**0.5
    return distance

def confidence_return(test_arr,data_plot): #this finds all the distances
    all_distance = []
    for i in data_plot:
        distance_val = distance(test_arr,i)
        all_distance.append(distance_val)
    return all_distance


test_array = []

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    try:
        test_arr,test_size = file_reader(f"test data/subject{no_var}.surprised.txt")
        test_array.append(test_arr)
    except:
        print('Exception2')
        continue
# below is the testing phase of the programme

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    try:
        test_arr,test_size = file_reader(f"yalefaces/subject{no_var}.surprised.txt")
        all_distance = confidence_return(test_arr,data_plot)
        index = all_distance.index(min(all_distance))
    except:
        continue
    
    subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
    
    print("\n")
    print("The minimum distance is: "+str(min(all_distance)))
    print("It most likely is: "+subj_arr[index//len(subj_arr)])
    print(f"random picker thinks it is subjet {random.randint(1,16)}")
print(len(file_names_in_test_set))

#single unit testing

"""
test_arr,test_size = file_reader(f"yalefaces/subject{no_var}.surprised.txt")
all_distance = confidence_return(test_arr,data_plot)
index = all_distance.index(min(all_distance))
print(all_distance,end=("\n"))    
print("{}{}".format("The index is: ",index))
subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
print("\n")
print("The minimum distance is: "+str(min(all_distance)))
print("It most likely is: "+subj_arr[index//10])
"""

# data visualisation is here

data_plot.append(test_array[2])
with_mystery_vector = data_plot
print(len(with_mystery_vector))

new_numpy_arr = np.array(with_mystery_vector)
print(new_numpy_arr.shape)
X_embedded = TSNE(n_components=2).fit_transform(new_numpy_arr)
subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
color_arr = ["black","red","darkorange","gold","yellow","lawngreen","turquoise","teal","cadetblue","slategrey","navy","blueviolet","indigo","thistle","pink"]
"""
counter = 0

for i in range(len(color_arr)):
    for j in range(len(file_names_in_test_set)):
        try:
            x,y = X_embedded[counter+j][0],X_embedded[counter+j][1]
            plt.scatter(x,y,color=f"{color_arr[i]}")
            #plt.annotate(subj_arr[i],(x,y))
            counter += 1
        except:
            print("Exception3")
            continue

print(counter)
#the last one is the mystery vector 
mx,my = X_embedded[-1][0],X_embedded[-1][1]
print((mx,my))
plt.scatter(mx,my,color="darkkhaki")
plt.annotate("Mystery vector(subject 3)",(mx,my))
plt.show()

"""
from PIL import Image

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
    return data_array,size

for i in range(1,16):
    for j in range(2):
        if j == 0:
            vector,size = file_reader("database/simple_database/datapoints/"+"subject"+str(i)+"-n.txt")
            data_plot.append(vector)
        elif j == 1:
            vector,size = file_reader("database/simple_database/datapoints/"+"subject"+str(i)+"-nn.txt")
            data_plot.append(vector)

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

for i in range(1,16):
    test_arr,test_size = file_reader("database/simple_database/test_datapoints/"+"subject"+str(i)+"-test.txt")
    all_distance = confidence_return(test_arr,data_plot)
    index = all_distance.index(min(all_distance))
    subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
    
    print("\n")
    print("The minimum distance is: "+str(min(all_distance)))
    print("It most likely is: "+subj_arr[index//2])

#code below is for single test case

'''
test_arr,test_size = file_reader("database/simple_database/test_datapoints/"+"subject"+"9"+"-test.txt")
all_distance = confidence_return(test_arr,data_plot)
index = all_distance.index(min(all_distance))
subj_arr = ["subject1","subject2","subjec3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
print(all_distance,"\n")
print("The minimum distance is: "+str(min(all_distance)))
print("It most likely is: "+subj_arr[index//2])
'''

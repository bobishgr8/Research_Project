import insightface
import urllib
import urllib.request
import cv2
import numpy as np
from skimage import io
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

GENDERS = {0: 'female',1: 'male'}

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

def read_picture(path):
    img = io.imread(path)
    stacked = np.stack((img,img,img),axis=2)
    return stacked,img

def get_features(stacked):
    model = insightface.app.FaceAnalysis()
    model.prepare(ctx_id=-1,nms=0.4)
    image = model.get(stacked)
    return image[0].embedding

#change the length of this array to control the ratio of training data to test ratio 
file_names_in_test_set = ["glasses", "happy", "leftlight", "noglasses", "normal", "rightlight", "sad", "sleepy", "wink"]

database_array = []

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    for j in file_names_in_test_set:
        img = io.imread(f"yalefaces/subject{no_var}.{str(j)}.jpg")
        stacked = np.stack((img,img,img),axis=2)
        database_array.append(get_features(stacked))

test_arr = []

# here is the part that runs the testing and the clasification
for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    img = io.imread(f"test data/subject{no_var}.surprised.jpg")
    stacked = np.stack((img,img,img),axis=2)
    test_arr.append(get_features(stacked))


for i in test_arr:
    all_distance = confidence_return(i,database_array)
    index = all_distance.index(min(all_distance))
    
    subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
    
    print("\n")
    print(f"The minimum distance is: {min(all_distance)}")
    print(f"It most likely is:{subj_arr[index//len(file_names_in_test_set)]}")

print(len(test_arr))


database_array.append(test_arr[2])
new_arr = np.array(database_array)
print(new_arr.shape)


#below this part is how we plot the graph and visualise the data

X_embedded = TSNE(n_components=2).fit_transform(new_arr)    
subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
color_arr = ["black","red","darkorange","gold","yellow","lawngreen","turquoise","teal","cadetblue","slategrey","navy","blueviolet","indigo","thistle","pink"]

counter = 0

for i in range(len(color_arr)):
    for j in range(len(file_names_in_test_set)):
        try:
            x,y = X_embedded[counter+j][0],X_embedded[counter+j][1]
            plt.scatter(x,y,color=f"{color_arr[i]}")
            #plt.annotate(subj_arr[i],(x,y))
            counter += 1
        except:
            print("exception3")
            continue

print(counter)
#the last one is the mystery vector 
mx,my = X_embedded[-1][0],X_embedded[-1][1]
print((mx,my))
plt.scatter(mx,my,color="darkkhaki")
plt.annotate("Mystery vector(subject 3)",(mx,my))
plt.show()

import insightface
import urllib
import urllib.request
import cv2
import numpy as np
from skimage import io

file_names_in_test_set = ["centerlight"] 
#"glasses", "happy", "leftlight", "noglasses", "normal", "rightlight", "sad", "sleepy", "wink"]

GENDERS = {0: 'female',1: 'male'}
database_array = []

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

# below code is for forming the array needed to compare the images

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    for j in file_names_in_test_set:
        img = io.imread(f"yalefaces/subject{no_var}.{str(j)}.jpg")
        stacked = np.stack((img,img,img),axis=2)

        model = insightface.app.FaceAnalysis()
        model.prepare(ctx_id=-1,nms=0.4)
        faces = model.get(stacked)

        for idx, face in enumerate(faces):
            '''
            bbox = face.bbox.astype(np.int)
            cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]),(0,255,0))

            for landmark in face.landmark.astype(np.int):
                cv2.line(img, (landmark[0]-3, landmark[1]), (landmark[0]+3,landmark[1]), (0,0,255))
                cv2.line(img, (landmark[0], landmark[1]-3), (landmark[0], landmark[1]+3),(0,0,255))
            '''
            #cv2.putText(img, f'#{idx} {GENDERS[face.gender]}|{face.age}',(bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0))
            database_array.append(face.embedding)

testing_array = []

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
        img = io.imread(f"test data/subject{no_var}.surprised.jpg")
        stacked = np.stack((img,img,img),axis=2)
        
        model = insightface.app.FaceAnalysis()
        model.prepare(ctx_id=-1,nms=0.4)
        faces = model.get(stacked)

        for idx, face in enumerate(faces):
            '''
            bbox = face.bbox.astype(np.int)
            cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]),(0,255,0))

            for landmark in face.landmark.astype(np.int):
                cv2.line(img, (landmark[0]-3, landmark[1]), (landmark[0]+3,landmark[1]), (0,0,255))
                cv2.line(img, (landmark[0], landmark[1]-3), (landmark[0], landmark[1]+3),(0,0,255))
            '''
            #cv2.putText(img, f'#{idx} {GENDERS[face.gender]}|{face.age}',(bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0))
        testing_array.append(face.embedding)

for i in testing_array:
    all_distance = confidence_return(i,database_array)
    index = all_distance.index(min(all_distance))
    
    subj_arr = ["subject1","subject2","subject3","subject4","subject5","subject6","subject7","subject8","subject9","subject10","subject11","subject12","subject13","subject14","subject15"]
    
    print("\n")
    print(f"The minimum distance is: {min(all_distance)}")
    print(f"It most likely is:{subj_arr[index//10]}")

print(len(testing_array))


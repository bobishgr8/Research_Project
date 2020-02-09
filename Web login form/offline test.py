from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import insightface
import urllib
import urllib.request
import cv2
import numpy as np
from skimage import io
import os

class user():
    def __init__(self,name,pictures,feature):
        self.name = name
        self.pictures = [pictures]
        self.features = [feature]
    
    def add_feature(self,new_image,feature_list):
       self.pictures.append(new_image)
       self.features.append(feature_list)

def distance(arr1,arr2):
    diff = []
    for i in range(arr1.shape[0]):
        diff.append((float(arr2[i])-float(arr1[i]))**2)
    distance = sum(diff)**0.5
    return distance

def confidence_return(test_arr,data_plot): #this finds all the distances
    all_distance = []
    for i in data_plot:
        distance_val = distance(test_arr,i)
        all_distance.append(distance_val)
    return min(all_distance)

def read_BNW(path):
    img = io.imread(path)
    stacked = np.stack((img,img,img),axis=2)
    return stacked,img

def read_rgb_picture(path):
    img = cv2.imread(path)
    return img

def get_features(stacked):
    model = insightface.app.FaceAnalysis()
    model.prepare(ctx_id=-1,nms=0.4)
    image = model.get(stacked)
    return image[0].embedding
'''
img = get_features(read_rgb_picture("static/Images/user (1).png"))
session_data = []
session_data_vectors = []
user = user("potato","static/Images/user (1).png",img)
user.add_feature("static/Images/user.png",get_features(read_rgb_picture("static/Images/user.png")))
session_data.append(user)
mystery_vector = get_features(read_rgb_picture("static/Images/user (2).png"))
session_data_vectors = []
for user in session_data:
    session_data_vectors.append(user.features)
all_distance = []
print(mystery_vector.shape)

for user in session_data_vectors:
    minimum_val = confidence_return(mystery_vector,user)
    print(minimum_val)   
'''

def feature_process_return(user,img):
    GENDERS = {0: 'female',1: 'male',}
    
    model = insightface.app.FaceAnalysis()
    model.prepare(ctx_id=-1,nms=0.4)
    image = model.get(img)

    for idx, face in enumerate(image):
        bbox = face.bbox.astype(np.int)
        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]),(0,255,0))
        for landmark in face.landmark.astype(np.int):
            cv2.line(img, (landmark[0]-3, landmark[1]), (landmark[0]+3,landmark[1]), (0,0,255))
            cv2.line(img, (landmark[0], landmark[1]-3), (landmark[0], landmark[1]+3),(0,0,255))
            cv2.putText(img, f'#{idx}{GENDERS[face.gender]}|{face.age}',(bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0))
    filename = f"static/Images/Processed/{user}_processed_img.png"
    cv2.imwrite(filename, img) 
    return filename
yeet = feature_process_return("potato",cv2.imread("static/Images/user.png"))
print(os.path.exists(yeet))

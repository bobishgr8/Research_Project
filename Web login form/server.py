from flask import Flask,render_template,request
from PIL import Image
import insightface
import urllib
import urllib.request
import cv2
import numpy as np
from skimage import io
import os

app = Flask(__name__)
global user_number 
# user number is the state of the system
user_number = 0


class user():
    def __init__(self,name,pictures,feature):
        self.name = name
        self.pictures = [pictures]
        self.features = [feature]
    
    def add_feature(self,new_image,feature_list):
       self.pictures.append(new_image)
       self.features.append(feature_list)


file_handle = open("user_list.txt","a+")
session_data = []
names = []

for i in file_handle:
    line = i.strip().split(",")
    if line[0] not in names:
        name = line[0]
        user = user(name,line[1],line[2])
        session_data.append(user)
        names.append(user.name)
    else:
        session_data[names.index(line[0])].pictures.append(line[1])
        session_data[names.index(line[0])].pictures.append(line[2])

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

def treshold_check(user_distance,mystery_vector_distance,treshold=15):
    if len(user_distance) > 2:
        mean_user_distance = sum(user_distance)/len(user_distance)
        treshold = mean_user_distance
        if mystery_vector_distance < treshold:
            return True
        else:
            return False
    else:
        if mystery_vector_distance < treshold:
            return True
        else:
            return False

def feature_process_return(user,img_path):
    try:
        img = cv2.imread(img_path)
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
        #if image[0].embedding == None:
        #    raise TypeError
    except TypeError:
        return "No face has been detected in the image uploaded to the server. Please try again."
    else:
        return filename,image[0].embedding

@app.route('/')
def landing_page_login():   
    return render_template("landing.html")

@app.route('/login')
def login_page():
    return render_template("Login_page.html")

@app.route('/register')
def registration():
    return render_template("register_form.html")

@app.route("/add", methods=["POST"])
def add_user():
    global user_number 
    new_user,user_disc = request.form["name"], request.form["description"]
    if new_user in names:
        return "person is already registered"
    if user_number == 0:
        user_picture = "user.png"
        file_path = f"static/Images/{user_picture}"
        processed_file_path,feature_vector = feature_process_return(new_user,file_path)
        print(feature_vector.shape)
        user_number += 1
        new_user = user(new_user,file_handle,feature_vector)
        session_data.append(new_user)
        names.append(new_user.name)
        file_handle.write(f"{new_user.name},{new_user.pictures},{new_user.features}")
        return render_template("sucessful_registration.html",image=processed_file_path)
    else:
        user_picture = f"user ({user_number}).png"
        file_path = f"static/Images/{user_picture}"
        processed_file_path,feature_vector = feature_process_return(new_user,file_path)        
        print(feature_vector.shape)
        user_number += 1
        new_user = user(new_user,file_handle,feature_vector)
        session_data.append(new_user)
        names.append(new_user.name)
        file_handle.write(f"{new_user.name},{new_user.pictures},{new_user.features}")
        return render_template("sucessful_registration.html",image=processed_file_path)

# byond this point it is mostly image processing for login

@app.route("/login_auth", methods=["POST"])
def login_auth():
    global user_number
    user = request.form["name"]
    if user not in names:
        user_number += 1
        return "unsucessful login please try again"
    login_picture = f"static/Images/user ({user_number}).png"
    user_number += 1
    mystery_vector = get_features(read_rgb_picture(login_picture))
    session_data_vectors = []
    for users in session_data:
        session_data_vectors.append(users.features)
    all_distance = []
    for plot in session_data_vectors:
        all_distance.append(confidence_return(mystery_vector,plot))
    print(all_distance)

    index = all_distance.index(min(all_distance))
    if session_data[index].name == user and treshold_check(session_data[index].features,min(all_distance)):
        session_data[index].add_feature(login_picture,mystery_vector)
        file_handle.write(f"{user},NIL,{login_picture},{list(mystery_vector)}\n")
        return f"login sucessful, welcome {user}"
    else:
        return f"Authentication failed. Either you are not {user} or try a different lighting condition"
    
if __name__ == '__main__':
    app.run(debug=True)
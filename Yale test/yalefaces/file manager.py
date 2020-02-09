import os
from PIL import Image
file_names_in_test_set = ["centerlight", 
"glasses", "happy", "leftlight", "noglasses", "normal", "rightlight", 
"sad", "sleepy", "wink"]

def grey_scale_convert(path):
    image_file = Image.open(path)
    image_file = image_file.convert('L') 
    os.remove(path)
    image_file.save(path)

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    for j in file_names_in_test_set:
        print(os.path.exists(f"yalefaces/subject{no_var}.{str(j)}.jpg"))
        grey_scale_convert(f"yalefaces/subject{no_var}.{str(j)}.jpg")

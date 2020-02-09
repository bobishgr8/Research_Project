#This file is to convert the training data to matrix data


from PIL import Image
def picture_to_matrix(file_name):
    try:
        img = Image.open(file_name)
    except:
        print("Error file specified does not exist")
    else:
        img = Image.open(file_name)
        grey = img.convert("LA")
        with Image.open(file_name) as image: 
            width, height = image.size
        print(width)
        print(height)
        data = grey.load()

        holding_img_data = [] 
        for x in range(width):
            for y in range(height):
                holding_img_data.append(data[x,y])
        img_data = []
        for cord in holding_img_data:
            img_data.append(cord[0])

        # now we write this to a file
        file_handle = open(str(file_name).strip(".jpg")+".txt","w")
        for i in img_data:
            file_handle.write(str(i)+",")
        file_handle.write(str(width)+",")
        file_handle.write(str(height)+",")
        file_handle.close()

file_names_in_test_set = ["centerlight", 
"glasses", "happy", "leftlight", "noglasses", "normal", "rightlight", 
"sad", "sleepy", "wink"]

#below is for running conversion

for i in range(1,16):
    if len(str(i)) < 2:
        no_var = "0"+str(i)
    else:
        no_var = str(i)
    for j in file_names_in_test_set:
        picture_to_matrix("yalefaces/"+"{}{}{}{}{}".format("subject",no_var,".",str(j),".bmp"))



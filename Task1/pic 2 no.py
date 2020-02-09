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

for i in range(1,16):
    for j in range(2):
        if j == 0:
            picture_to_matrix("database/simple_database/datapoints"+"subject"+str(i)+"-nn")
        if j == 1:
            picture_to_matrix("database/simple_database/datapoints"+"subject"+str(i)+"-nn")
        

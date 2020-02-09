import hashlib
from PIL import Image

file_name = input("please input the file name of this image\n")
def picture_to_matrix(file_name):
    try:
        img = Image.open(file_name) 
        #we check if the image file is existent
    except:
        print("Error file specified does not exist")
        #error if the file is not found :(
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

picture_to_matrix(file_name)
#all of of the above code is to turn an image into numbers and store its .txt file
#so all the input we need from the user is simply what the file name is

#this is the main function that will hash the files and return the MD5 string
def md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(4096), b""):
            hash_md5.update(chunk)
    file_handle.close()
    return hash_md5.hexdigest()

#these are the "Database" that we will be testing

database = []
#we mannually input the hashes into the "database"
database.append(md5("face1.txt"))
database.append(md5("face2.txt"))
database.append(md5("face3.txt"))
database.append(md5("face4.txt"))
database.append(md5("face5.txt"))


#checking if the MD5 of an image is withn the databse:
if md5(str(file_name).strip(".jpg")+".txt") in database:
    print("it is in the database")
else:
    print("it is not in the database")







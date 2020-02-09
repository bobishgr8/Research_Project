from PIL import Image
from random import randint as yeet
import numpy as np
pic_colour = []

for i in range(1,255):
    pic_colour.append((yeet(1,255) for i in range(3)))
    
size = (254,254)
img = Image.new("RGB",size)
data = np.array([pic_colour]*254)
print(data)

img.putdata(data)
img.save("hello.jpg")

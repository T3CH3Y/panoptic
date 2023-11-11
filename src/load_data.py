import pinecone
import os
from PIL import Image
import numpy as np

dir = os.listdir("photos")
for file_name in dir:
    im = Image.open("photos/" + file_name)
    rgb_data = np.array(im)

    red = rgb_data[:,:,0].flatten()
    green = rgb_data[:,:,1].flatten()
    blue = rgb_data[:,:,2].flatten()
    image_pixels = red.size

    red_histogram, red_bin = np.histogram(red, bins=256, range =(0, 255)) 
    green_histogram, green_bin = np.histogram(green, bins=256, range =(0, 255)) 
    blue_histogram, blue_bin = np.histogram(blue, bins=256, range =(0, 255))
    
    norm_red = red_histogram/image_pixels
    norm_green = green_histogram/image_pixels
    norm_blue = blue_histogram/image_pixels

print(image_pixels)
    

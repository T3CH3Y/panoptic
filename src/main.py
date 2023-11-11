import pinecone
from options import config
import numpy as np
from PIL import Image

pinecone.init(
    api_key = config["pinecone"]["api_key"],
    environment = config["pinecone"]["environment"]
)

index = pinecone.Index(config["pinecone"]["index"])

test_path = "photos/Hieronymus_Bosch_14.jpg"

def vectorize(img_path):

    im = Image.open(img_path)
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

    img_vec = np.concatenate((norm_red, norm_green, norm_blue)) * 100

    return img_vec.tolist()

img_vector = vectorize(test_path)
query_response = index.query(top_k = 1, vector = img_vector)

print(query_response)

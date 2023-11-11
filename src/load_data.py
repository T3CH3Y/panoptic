import pinecone
import os
from PIL import Image
import numpy as np

dir = os.listdir("photos")
for file_name in dir:
    im = Image.open("photos/" + file_name)
    im_matrix = np.array(im)
    print(im_matrix[0][0])

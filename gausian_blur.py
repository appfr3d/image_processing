import numpy as np 
from utils import convolve, get_image, save_image

image_name = 'image_0'
image = get_image('images/original/' + image_name + '.jpg')

# TODO: implement a function that creates a real gausien kernel
# https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

''' 
# A 11x11 filled with a single value
filter_size = 11 # must be odd
filter_value = 1 
gaus = np.full((filter_size, filter_size), filter_value) / (filter_size*filter_size*filter_value)
'''

# static gaus kernel
gaus = np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1],
]) / 256

blurred = convolve(image, gaus)

save_location = 'images/gausian_blur/' + image_name +  '_gausian_blur_size_' + str(gaus.shape[0]) + '.jpg'
save_image(blurred, save_location)

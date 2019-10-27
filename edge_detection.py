import numpy as np 
from utils import convolve, get_image, save_image
from grayscale import grayscale_mean
from gausian_blur import gausian_blur

def edge_detection(im):
	'''
	Function that convolves im with vertial and horizontal sobel filters
	to find edges in a photo

	Args:
		im: np.array of shape [H, W, 3]
	'''
	image = gausian_blur(im, 5, 1.4)

	image = grayscale_mean(image)

	# Using vertical and horizontal Sobel kernels 
	sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

	edge_x = convolve(image, sobel_x)
	edge_y = convolve(image, sobel_y)
	edge = np.round(np.sqrt(np.power(edge_x, 2) + np.power(edge_y, 2)))

	return edge, edge_x, edge_y


if __name__ == "__main__":
	image_name = 'image_0'
	original_image = get_image('images/original/' + image_name + '.jpg')

	edge, edge_x, edge_y = edge_detection(original_image)

	save_location_x = 'images/edge_detection/' + image_name +  '_edge_detection_x_.jpg'
	save_image(edge_x, save_location_x)

	save_location_y = 'images/edge_detection/' + image_name +  '_edge_detection_y_.jpg'
	save_image(edge_y, save_location_y)

	save_location = 'images/edge_detection/' + image_name +  '_edge_detection_.jpg'
	save_image(edge, save_location)


import numpy as np 
from utils import convolve, get_image, save_image
from grayscale import grayscale_mean

def edge_detection(im):
	'''
	Function that convolves im with vertial and horizontal sobel filters
	to find edges in a photo

	Args:
		im: np.array of shape [H, W, 3]
	'''
	image = grayscale_mean(im)

	# Using vertical and horizontal Sobel kernels 
	sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

	edge_x = convolve(image, sobel_x)
	edge_y = convolve(image, sobel_y)
	edge = np.round(np.sqrt(np.power(edge_x, 2) + np.power(edge_y, 2)))

	return edge, edge_x, edge_y



# Convert to grayscale
# r, b, g = original_image[:,:,0], original_image[:,:,1], original_image[:,:,2]

# the shape is being manipulated here...
# image = np.round((r+b+g)*(1/3))

# make the image to a grayscale
# image = grayscale_mean(original_image)
# image = np.zeros(original_image.shape)
# for row, col in np.ndindex(original_image.shape[:-1]): # iterate over row and col, not color
# 	mean_val = np.mean(original_image[row, col])
# 	image[row, col, :] = np.full(original_image.shape[2], mean_val)

# Using vertical and horizontal Sobel kernels 
# sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
# sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# edge_x = convolve(image, sobel_x)
# edge_y = convolve(image, sobel_y)
# edge = np.round(np.sqrt(np.power(edge_x, 2) + np.power(edge_y, 2)))



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


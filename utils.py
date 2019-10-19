import numpy as np
from PIL import Image

def convolve(im, kernel):
	''' 
	A function that convolves im with kernel. The edges outside the image is handled as 0
	
	Args:
		im: np.array of shape [H, W, 3]
		kernel: np.array of shape [K, K]
	
	Returns:
		np.array of shape [H, W, 3]
	'''

	padding = int((kernel.shape[0]-1)/2)

	# add a border of zeros to make life simpler inside the for-loops
	# pads im with zero in top, bottom, left, right, but not in color
	pad_im = np.pad(im, ((padding,padding), (padding,padding), (0,0)), 'constant')

	convolved = np.zeros(im.shape)

	for row in range(padding, im.shape[0] + padding): # rows
		for col in range(padding, im.shape[1] + padding): # columns
			for color in range(im.shape[2]): # colors
				# pick out a part of the image
				part = pad_im[row-padding:row+padding+1, col-padding:col+padding+1, color]

				value = int(round(sum(sum(kernel*part))))

				# setting the value
				convolved[row-padding, col-padding, color] = value

	return convolved

def get_image(loaction):
	image = Image.open(location)
	return np.array(image)

def save_image(im, location):
	image = Image.fromarray(im.astype('uint8'))
	image.show()
	image.save(location)
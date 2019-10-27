import numpy as np 
from utils import convolve, get_image, save_image
import matplotlib.pyplot as plt

def gausian_kernel(size, sigma=1):
	''' 
	A function that creates a gausian kernel.
	
	Args:
		size: int, an odd number defining the height and width of the kernel
		sigma: int, roughtness paramater
	
	Returns:
		np.array of shape [size//2, size//2]
	'''

	size = int(size) // 2
	x, y = np.mgrid[-size:size+1, -size:size+1]
	normal = 1.0/(2.0 * np.pi * sigma**2)
	return np.exp(-((x**2 + y**2) / (2.0 * sigma**2))) * normal


def gausian_blur(im, kernel=gausian_kernel(5)):
	''' 
	A function that convolves im with kernel.
	
	Args:
		im: np.array of shape [H, W, 3]
		kernel: nparray of shape [S, S]
	
	Returns:
		np.array of shape [H, W, 3]
	'''
	return convolve(im, kernel)


if __name__ == "__main__":
	image_name = 'image_0'
	image = get_image('images/original/' + image_name + '.jpg')

	# show the effect of changing sigma
	for i in range(1, 8, 2):
		g = gausian_kernel(21, i)
		plt.imshow(g, cmap='gray')
		plt.show()

	# the actual blurring
	size, sigma = 11, 1.4
	kernel = gausian_kernel(size, sigma)
	blurred = gausian_blur(image, kernel)
	save_image(blurred, 'images/gausian_blur/' + image_name +  '_gausian_blur_size_' + str(size) + '_sigma_' + str(sigma) + '.jpg')

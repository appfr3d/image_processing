import numpy as np 
from utils import convolve, get_image, save_image

def pixelate(im, pixel_size):
	'''
	Function that reduces the amount of pixels in a image

	Args:
		im: np.array of shape [H, W, 3]
		pixel_size: int, an odd number defining how many pixels from the original 
					image that each pixel in the new image shoult have 

	Returns:
		np.array of shape [H/pixel_size, W/pixel_size, 3]
	'''
	kernel = np.ones((pixel_size, pixel_size)) / pixel_size**2
	pixelated = np.zeros((im.shape[0]//pixel_size, im.shape[1]//pixel_size, im.shape[2]))

	for row in range(pixelated.shape[0]):
		for col in range(pixelated.shape[1]):
			for color in range(pixelated.shape[2]):
				part = im[row*pixel_size:row*pixel_size+pixel_size, col*pixel_size:col*pixel_size+pixel_size, color]
				pixelated[row, col, color] = int(round(sum(sum(part*kernel))))

	return pixelated


if __name__ == "__main__":
	image_name = 'image_0'
	original_image = get_image('images/original/' + image_name + '.jpg')

	size = 5
	pixelated = pixelate(original_image, size)

	save_location = 'images/pixelated/' + image_name +  '_pixelated_size_' + str(size) + '.jpg'
	save_image(pixelated, save_location)
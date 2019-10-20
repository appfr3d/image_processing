import numpy as np 
from utils import get_image, save_image

def grayscale_mean(im):
	mean = np.zeros(im.shape) # set rgb as the mean of rgb
	for row, col in np.ndindex(im.shape[:-1]): # iterate over row and col, not color
		mean_val = np.mean(im[row, col])
		mean[row, col] = np.full(im.shape[2], mean_val)
	return mean

def grayscale_maxi(im):
	maxi = np.zeros(im.shape) # set rgb as the max of rgb
	for row, col in np.ndindex(im.shape[:-1]): # iterate over row and col, not color
		maxi_val = np.max(im[row, col])
		maxi[row, col] = np.full(im.shape[2], maxi_val)
	return maxi

def grayscale_mini(im):
	mini = np.zeros(im.shape) # set rgb as the min of rgb
	for row, col in np.ndindex(im.shape[:-1]): # iterate over row and col, not color
		mini_val = np.min(im[row, col])
		mini[row, col] = np.full(im.shape[2], mini_val)
	return mini

def grayscale_all(im):
	mean = np.zeros(im.shape) # set rgb as the mean of rgb
	maxi = np.zeros(im.shape) # set rgb as the max of rgb
	mini = np.zeros(im.shape) # set rgb as the min of rgb

	for row, col in np.ndindex(im.shape[:-1]): # iterate over row and col, not color
		mean_val = np.mean(im[row, col])
		mean[row, col] = np.full(im.shape[2], mean_val)
		
		maxi_val = np.max(im[row, col])
		maxi[row, col] = np.full(im.shape[2], maxi_val)

		mini_val = np.min(im[row, col])
		mini[row, col] = np.full(im.shape[2], mini_val)
	return mean, maxi, mini

# mean_image = Image.fromarray(mean.astype('uint8'))
# mean_image.show()

# maxi_image = Image.fromarray(maxi.astype('uint8'))
# maxi_image.show()

# mini_image = Image.fromarray(mini.astype('uint8'))
# mini_image.show()


# mean_image.save('images/grayscale/' + image_name +  '_grayscale_mean.jpg')
# maxi_image.save('images/grayscale/' + image_name +  '_grayscale_maxi.jpg')
# mini_image.save('images/grayscale/' + image_name +  '_grayscale_mini.jpg')

if __name__ == "__main__":
	image_name = 'image_0'
	image = get_image('images/original/' + image_name + '.jpg')

	mean, maxi, mini = grayscale_all(image)

	save_image(mean, 'images/grayscale/' + image_name +  '_grayscale_mean.jpg')
	save_image(maxi, 'images/grayscale/' + image_name +  '_grayscale_maxi.jpg')
	save_image(mini, 'images/grayscale/' + image_name +  '_grayscale_mini.jpg')

	# im = plt.imread("images/lake.jpg")
	# im = greyscale(im)
	# inverse_im = inverse(im)
	# save_im("lake_greyscale.jpg", im, cmap="gray")
	# save_im("lake_inverse.jpg", inverse_im, cmap="gray")


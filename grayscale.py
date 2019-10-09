import numpy as np 
from PIL import Image

image_name = 'image_0'
picture = Image.open('./images/original/' + image_name + '.jpg')
array = np.array(picture)

mean = np.zeros(array.shape) # set rgb as the mean of rgb
maxi = np.zeros(array.shape) # set rgb as the max of rgb
mini = np.zeros(array.shape) # set rgb as the min of rgb

for row, col in np.ndindex(array.shape[:-1]): # iterate over row and col, not color
	mean_val = np.mean(array[row][col])
	mean[row][col] = np.full(array.shape[2], mean_val)
	
	maxi_val = np.max(array[row][col])
	maxi[row][col] = np.full(array.shape[2], maxi_val)

	mini_val = np.min(array[row][col])
	mini[row][col] = np.full(array.shape[2], mini_val)

mean_image = Image.fromarray(mean.astype('uint8'))
mean_image.show()

maxi_image = Image.fromarray(maxi.astype('uint8'))
maxi_image.show()

mini_image = Image.fromarray(mini.astype('uint8'))
mini_image.show()


mean_image.save('images/grayscale/' + image_name +  '_grayscale_mean.jpg')
maxi_image.save('images/grayscale/' + image_name +  '_grayscale_maxi.jpg')
mini_image.save('images/grayscale/' + image_name +  '_grayscale_mini.jpg')

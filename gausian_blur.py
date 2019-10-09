import numpy as np 
from PIL import Image

image_name = 'image_0'
picture = Image.open('images/original/' + image_name + '.jpg')
array = np.array(picture)

blurred = np.zeros(array.shape)

print(array.shape) # (rows, columns, colors)

filter_size = 11 # must be odd
filter_value = 1 

# the range to loop over for our filter
start = int(-((filter_size - 1) / 2))	
end   = int(((filter_size - 1) / 2) + 1)

gaus = np.full((filter_size, filter_size), filter_value)

for row in range(array.shape[0]): # rows
	for col in range(array.shape[1]): # columns
		for color in range(array.shape[2]): # colors
			value = 0 # the total value of pixels
			num_values = 0 # will most times be filter_size^2, but not on the edges
			for r in range(start, end):
				for c in range(start, end):
					if row + r > 0 and row + r < array.shape[0] and col + c > 0 and col + c < array.shape[1]:
						# we are inside the bounds
						value += gaus[r][c]*array[row+r][col+c][color]
						num_values += 1

			blurred[row][col][color] = value/num_values # mean of the values

blurred_image = Image.fromarray(blurred.astype('uint8'))
blurred_image.show()

blurred_image.save('images/gausian_blur/' + image_name +  '_gausian_blur_size_' + str(filter_size) + '.jpg')

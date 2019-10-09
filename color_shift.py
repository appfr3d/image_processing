import numpy as np 
from PIL import Image

image_name = 'image_0'
picture = Image.open('images/original/' + image_name + '.jpg')
array = np.array(picture)

rgb_shift = [(-5,5), (0,0), (5,-5)]

min_x = abs(min(rgb_shift, key=lambda x: x[0])[0])
max_x = abs(max(rgb_shift, key=lambda x: x[0])[0])

min_y = abs(min(rgb_shift, key=lambda x: x[1])[1])
max_y = abs(max(rgb_shift, key=lambda x: x[1])[1])

# shifted = np.zeros(array.shape + (min_x + max_x, min_y + max_y, 0))

shifted = np.zeros(tuple(map(sum,zip(array.shape, (min_x + max_x, min_y + max_y, 0)))))

# tuple(map(sum,zip(array.shape, (min_x + max_x, min_y + max_y, 0))))

print(array.shape)
print(shifted.shape)

for row in range(array.shape[0]): # rows
	for col in range(array.shape[1]): # columns
		for color in range(array.shape[2]): # colors
			shift = rgb_shift[color]
			shifted[row+min_y+shift[0]][col+min_x+shift[1]][color] = array[row][col][color]

			'''
			value = 0 # the total value of pixels
			num_values = 0 # will most times be filter_size^2, but not on the edges
			for r in range(start, end):
				for c in range(start, end):
					if row + r > 0 and row + r < array.shape[0] and col + c > 0 and col + c < array.shape[1]:
						# we are inside the bounds
						value += gaus[r][c]*array[row+r][col+c][color]
						num_values += 1

			blurred[row][col][color] = value/num_values # mean of the values
			'''

shifted_image = Image.fromarray(shifted.astype('uint8'))
shifted_image.show()

shifted_image.save('images/color_shift/' + image_name +  '_color_shift.jpg')

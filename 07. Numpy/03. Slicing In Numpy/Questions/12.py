# A simple grayscale image can be represented as a 2D NumPy array where each number represents pixel intensity.

import numpy as np
image = np.array([
        [10, 20, 30, 40, 50],
        [20, 30, 40, 50, 60],
        [30, 40, 50, 60, 70],
        [40, 50, 60, 70, 80],
        [50, 60, 70, 80, 90]
])
# Tasks:
# Find the dimensions of the image.
# Find its shape.
# Find the total number of pixels.
# Display the center pixel.
# Extract the top-left 3 × 3 region.
# Extract the bottom-right 2 × 2 region.
# Increase the intensity of the center 3 × 3 region by 20.
# Display the modified image


print(image.ndim)

print(image.shape)

print(image.size)

print(image[2 , 2])

print(image[:3 , :3])

print(image[-2: , -2:])

image[1:4 , 1:4] += 20
print(image[1:4 , 1:4])

print(image) 
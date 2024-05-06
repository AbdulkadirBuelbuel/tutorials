# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
img_1 = cv2.imread("./tutorials/data/images/logo.png", cv2.IMREAD_COLOR)
img_2 = cv2.imread("./tutorials/data/images/logo.png", cv2.IMREAD_GRAYSCALE)

# TODO Do some print out about the loaded data using type, dtype and shape
print(type(img_1))
print(type(img_2))

print(img_1.shape)
print(img_2.shape)

print(img_1.dtype)
print(img_2.dtype)
# TODO Continue with the grayscale image
img = img_2
# TODO Extract the size or resolution of the image

h,w =img.shape
# TODO Resize image
img= cv2.resize(img, (8,4))
# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
print(img[0,:])
# TODO Print first column
print(img[:,0])

# TODO Continue with the color image
img = img_1
# TODO Set an area of the image to black
#for i in range(100,200):
 #   for j in range(200):
  #      img[j][i]=(0,0,0)

img[100:160,:] = (0,0,0)


# TODO Show the image and wait until key pressed
cv2.imshow("title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# TODO Find all used colors in the image
print(img_1[cv2.IMREAD_COLOR])
# TODO Copy one part of an image into another one

# TODO Save image to a file

# TODO Show the image again

# TODO Show the original image (copy demo)

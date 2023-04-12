# Tutorial #9
# -----------
#
# Demonstrating Gaussian blur filter with OpenCV.

import cv2
import numpy as np
import time


# TODO Implement the convolution with opencv
def convolution_with_opencv(image, kernel):
    # Flip the kernel as opencv filter2D function is a
    # Correlation not a convolution

    # When ddepth=-1, the output image will have the same depth as the source.

    # Run filtering

    # Return result
    return


def show_kernel(kernel):
    # Show the kernel as image
    # Note that window parameters have no effect on MacOS
    title_kernel = "Kernel"
    cv2.namedWindow(title_kernel, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_kernel, 300, 300)

    # Scale kernel to make it visually more appealing
    kernel_img = cv2.normalize(kernel, kernel, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    cv2.imshow(title_kernel, kernel_img)
    cv2.waitKey(0)


def show_resulting_images(image, result):
    # Note that window parameters have no effect on MacOS
    title_original = "Original image"
    cv2.namedWindow(title_original, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title_original, image)

    title_result = "Resulting image"
    cv2.namedWindow(title_result, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title_result, result)

    key = cv2.waitKey(0)
    if key == ord("s"):
        # Save resulting image
        res_filename = "filtered_with_%dx%d_gauss_kernel_with_sigma_%d.png" % (kernel_size, kernel_size, sigma)
        cv2.imwrite(res_filename, result)
    cv2.destroyAllWindows()


# Load the image.
image_name = "./tutorials/data/images/Bumbu_Rawon.jpg"
image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
# image = cv2.resize(image, (320,213))

# TODO Define kernel
kernel = "TODO: define this variable"

# TODO Define kernel size
kernel_size = "TODO: define this variable"

# TODO Define Gaussian standard deviation (sigma). If it is non-positive,
# It is computed from kernel_size as
# sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
sigma = "TODO: define this variable"

# TODO Create the kernel with OpenCV

# Visualize the kernel
show_kernel(kernel)

# TODO Run convolution and measure the time it takes
# Start time to calculate computation duration
start = "TODO: define this variable"
# Run the convolution and write the resulting image into the result variable
result = "TODO: define this variable"

# End time after computation
end = "TODO: define this variable"

# Print timing results
print(
    "Computing the convolution of an image with a resolution of",
    image.shape[1],
    "by",
    image.shape[0],
    "and a kernel size of",
    kernel.shape[0],
    "by",
    kernel.shape[1],
    "took",
    end - start,
    "seconds.",
)

# Show the original and the resulting image
show_resulting_images(image, result)

# Tutorial #12
# ------------
#
# Select three points in two images and compute the appropriate affine transformation. Inspired by
# https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

import numpy as np
import cv2

# Define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []


# TODO Define one callback functions for each image window
def click_src(event, x, y, flags, param):
    # Grab references to the global variables
    global ref_pt_src
    # If the left mouse button was clicked, add the point to the source array

    # in if block: Draw a circle around the clicked point

    # in if block: Redraw the image


def click_dst(event, x, y, flags, param):
    # Grab references to the global variables
    global ref_pt_dst
    # If the left mouse button was clicked, add the point to the source array

    # in if block: Draw a circle around the clicked point

    # in if block: Redraw the image


# Load image and resize for better display
img = cv2.imread('data/images/nl_clown.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

# TODO Initialize needed variables and windows including mouse callbacks

# Keep looping until the 'q' key is pressed
computationDone = False
while True:

    # TODO If there are three reference points, then compute the transform and apply the transformation
    if not (computationDone):

        # TODO Display the image and wait for a keypress

        # TODO If the 'r' key is pressed, reset the transformation

        key = cv2.waitKey(10)

        # TODO If the 'q' key is pressed, break from the loop
        if key == ord("q"):
            break

cv2.destroyAllWindows()

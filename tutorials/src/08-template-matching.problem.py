# Tutorial #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example is
# counting blood cells
import cv2

use_color = True

if use_color:
    # Load image and template image, note that the template has been manually
    # cut out of the image
    img = cv2.imread("./tutorials/data/images/chewing_gum_balls06.jpg", cv2.IMREAD_COLOR)
    template = cv2.imread("./tutorials/data/images/cgb_green.jpg", cv2.IMREAD_COLOR)

    # Read shape of the template and original image
    h, w, c = template.shape
    H, W, C = img.shape
else:
    # Load image and template image, note that the template has been manually
    # cut out of the image
    img = cv2.imread("./tutorials/data/images/chewing_gum_balls06.jpg", cv2.IMREAD_GRAYSCALE)
    template = cv2.imread("./tutorials/data/images/cgb_green.jpg", cv2.IMREAD_GRAYSCALE)

    # Read shape of the template and original image
    h, w = template.shape
    H, W = img.shape
    # TODO Define template matching methods,
    # See https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the
    # math behind each method
methods= [

    cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF_NORMED
]
    # TODO Loop over all methods in order to compare them
for method in methods: 

    # TODO (In loop) work on a new image each time
    img = img_color.copy()

    # TODO (In loop) do the template matching
match_img = cv2.matchTemplate(img, template_color, method)

    # TODO (In loop) get the best match location
match_bin = cv2.threshold(match_img, 0.9, 1.0, cv2.THRESH_BINARY)
img= cv2.bitwise_and(img,img, mask = match_bin)

    # TODO (In loop) draw rectangle at found location

    # TODO (In loop) show original image with found location

    # TODO (In loop) show image with the template matching result for all pixels

    # (in loop) just press any key to show the next image
cv2.waitKey(0)

cv2.destroyAllWindows()

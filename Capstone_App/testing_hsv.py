import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

# initialize the video
# cap = cv2.VideoCapture(0)


# create color finder object
myColorFinder = ColorFinder(True)
# green ball
hsvVals = {'hmin': 21, 'smin': 51, 'vmin': 130, 'hmax': 31, 'smax': 133, 'vmax': 255}

# orange ball
hsvVals = {'hmin': 13, 'smin': 167, 'vmin': 181, 'hmax': 20, 'smax': 255, 'vmax': 255}
hsvVals = {'hmin': 10, 'smin': 202, 'vmin': 177, 'hmax': 18, 'smax': 240, 'vmax': 255}



while True:
    # success, img = cap.read()
    img = cv2.imread("approach_two.png")
    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Display
    img = cv2.resize(img, (0,0), None, .5, .5)
    imgColor = cv2.resize(imgColor, (0,0), None, .5, .5)
    cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgColor)

    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
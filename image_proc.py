import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('data/img2.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
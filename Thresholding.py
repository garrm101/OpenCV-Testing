import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test2.jpg', 0)
if img == None:
    raise ValueError('Image does not exist!')
height = np.size(img, 0)
width = np.size(img, 1)
block = int(np.round(np.sqrt((width * height * .0015)), 0))
block = block + 1 if block % 2 == 0 else block

a = 201

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, block, 10)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, a, 12)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

plt.imshow(images[0], 'gray')
plt.title(a)
plt.xticks([]), plt.yticks([])
plt.show()
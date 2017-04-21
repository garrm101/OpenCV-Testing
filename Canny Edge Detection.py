import cv2
import numpy as np
from matplotlib import pyplot as plt

a = 17

img = cv2.imread('test2.jpg', 0)
edges = cv2.Canny(img, a, a*5)
#plt.subplot(121), plt.imshow(img, cmap='gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122), plt.imshow(edges, cmap='gray')
#plt.imshow(cv2.bitwise_not(edges), 'gray')
plt.imshow(edges, 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

plt.ion()

# for i in range(100):
#     edges = cv2.Canny(img, i, i*5)
#     plt.title(i)
#     plt.imshow(edges, 'gray')
#     plt.pause(0.05)
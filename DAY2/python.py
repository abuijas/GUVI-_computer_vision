import cv2
import matplotlib.pyplot as plt

img = cv2.imread("READ PY.jpg")
medium = cv2.medianBlur(img,5)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
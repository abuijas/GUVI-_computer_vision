import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
print(img.shape)

cv2.circle(img,(20,20),60,(0,0,255),1)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
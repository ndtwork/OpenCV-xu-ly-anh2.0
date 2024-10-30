import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

project_dir = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv2.imread(image_path)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
negative_img = 255 - img

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('RGB')

plt.subplot(2, 2, 2)
plt.imshow(img_hsv)
plt.title('HSV')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Dương bản')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(negative_img, cv2.COLOR_BGR2RGB))
plt.title('Âm bản')

plt.tight_layout()
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Đọc ảnh gốc
project_dir = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.png")
img_color = cv2.imread(image_path)

# Chuyển đổi sang ảnh xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Tính toán histogram cho ảnh xám
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

# Tính toán histogram cho ảnh màu (từng kênh R, G, B)
colors = ('b', 'g', 'r')
hist_color = {}
for i, col in enumerate(colors):
    hist_color[col] = cv2.calcHist([img_color], [i], None, [256], [0, 256])

# Hiển thị ảnh và biểu đồ histogram
plt.figure(figsize=(12, 6))

# Hiển thị ảnh xám
plt.subplot(2, 3, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Ảnh xám')

# Hiển thị biểu đồ histogram của ảnh xám dưới dạng cột
plt.subplot(2, 3, 4)
plt.bar(range(256), hist_gray.ravel(), color='gray', width=1)
plt.title('Histogram - Ảnh xám')
plt.xlim([0, 256])

# Hiển thị ảnh màu
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.title('Ảnh màu')

# Hiển thị biểu đồ histogram của từng kênh màu
plt.subplot(2, 3, 5)
for col in colors:
    plt.plot(hist_color[col], color=col)
plt.title('Histogram - Ảnh màu (RGB)')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()

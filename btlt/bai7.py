import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Đọc ảnh gốc
project_dir = os.path.dirname(os.path.dirname(__file__))  # Lấy thư mục dự án
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img_color = cv2.imread(image_path)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)  # Chuyển ảnh màu sang ảnh xám

# 1. Lọc trung vị (Median Filter)
median_3x3 = cv2.medianBlur(img_color, 3)
median_9x9 = cv2.medianBlur(img_color, 9)

# 2. Lọc tối thiểu và tối đa
# Tạo một hàm lọc tối thiểu
def min_filter(image, ksize):
    return cv2.erode(image, np.ones((ksize, ksize), np.uint8))

# Tạo một hàm lọc tối đa
def max_filter(image, ksize):
    return cv2.dilate(image, np.ones((ksize, ksize), np.uint8))

# Áp dụng lọc tối thiểu và tối đa
min_filter_3x3 = min_filter(img_color, 3)
min_filter_9x9 = min_filter(img_color, 9)
max_filter_3x3 = max_filter(img_color, 3)
max_filter_9x9 = max_filter(img_color, 9)

# Hiển thị ảnh gốc và ảnh sau khi lọc
plt.figure(figsize=(12, 12))

# Ảnh gốc
plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.title('Ảnh gốc')

# Lọc trung vị 3x3
plt.subplot(3, 3, 2)
plt.imshow(cv2.cvtColor(median_3x3, cv2.COLOR_BGR2RGB))
plt.title('Lọc trung vị 3x3')

# Lọc trung vị 9x9
plt.subplot(3, 3, 3)
plt.imshow(cv2.cvtColor(median_9x9, cv2.COLOR_BGR2RGB))
plt.title('Lọc trung vị 9x9')

# Lọc tối thiểu 3x3
plt.subplot(3, 3, 4)
plt.imshow(cv2.cvtColor(min_filter_3x3, cv2.COLOR_BGR2RGB))
plt.title('Lọc tối thiểu 3x3')

# Lọc tối thiểu 9x9
plt.subplot(3, 3, 5)
plt.imshow(cv2.cvtColor(min_filter_9x9, cv2.COLOR_BGR2RGB))
plt.title('Lọc tối thiểu 9x9')

# Lọc tối đa 3x3
plt.subplot(3, 3, 6)
plt.imshow(cv2.cvtColor(max_filter_3x3, cv2.COLOR_BGR2RGB))
plt.title('Lọc tối đa 3x3')

# Lọc tối đa 9x9
plt.subplot(3, 3, 7)
plt.imshow(cv2.cvtColor(max_filter_9x9, cv2.COLOR_BGR2RGB))
plt.title('Lọc tối đa 9x9')

plt.tight_layout()
plt.show()

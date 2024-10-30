import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def histogram_stretching(image):
    # Tính giá trị min và max trong ảnh
    min_val = np.min(image)
    max_val = np.max(image)

    # Giãn histogram
    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

# Đọc ảnh gốc
project_dir = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img_color = cv2.imread(image_path)

# Chuyển ảnh sang ảnh xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Cân bằng histogram
equalized_img = cv2.equalizeHist(img_gray)

# Giãn histogram
stretched_img = histogram_stretching(img_gray)

# Hiển thị ảnh gốc, ảnh đã cân bằng và ảnh đã giãn histogram
plt.figure(figsize=(12, 8))

# Ảnh gốc
plt.subplot(1, 3, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Ảnh xám gốc')

# Ảnh đã cân bằng histogram
plt.subplot(1, 3, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Cân bằng Histogram')

# Ảnh đã giãn histogram
plt.subplot(1, 3, 3)
plt.imshow(stretched_img, cmap='gray')
plt.title('Giãn Histogram')

plt.tight_layout()
plt.show()

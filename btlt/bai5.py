import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Đọc ảnh từ thư mục dự án
project_dir = os.path.dirname(os.path.dirname(__file__))  # Lấy thư mục dự án
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv2.imread(image_path)

# Nếu ảnh là ảnh màu (3 kênh), chuyển nó sang ảnh xám
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hàm vẽ biểu đồ histogram dạng cột rộng
def plot_histogram_bar(image, title):
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))
    plt.bar(bin_edges[0:-1], histogram, color='blue', width=2)
    plt.title(title)
    plt.xlabel("Mức xám")
    plt.ylabel("Số lượng điểm ảnh")

# Hiển thị ảnh gốc và histogram
plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Ảnh gốc (img)")

plt.subplot(2, 3, 2)
plot_histogram_bar(img, "Histogram của ảnh gốc (img)")

# Thực hiện phép cân bằng biểu đồ (Histogram Equalization)
img_equalized = cv2.equalizeHist(img.astype(np.uint8))

# Hiển thị ảnh sau cân bằng và histogram của nó
plt.subplot(2, 3, 3)
plt.imshow(img_equalized, cmap='gray')
plt.title("Ảnh (img) sau khi cân bằng")

plt.subplot(2, 3, 4)
plot_histogram_bar(img_equalized, "Histogram sau khi cân bằng")

# Thực hiện phép giãn biểu đồ (Histogram Stretching)
def histogram_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

img_stretched = histogram_stretching(img)

# Hiển thị ảnh sau giãn biểu đồ và histogram của nó
plt.subplot(2, 3, 5)
plt.imshow(img_stretched, cmap='gray')
plt.title("Ảnh (img) sau khi giãn biểu đồ")

plt.subplot(2, 3, 6)
plot_histogram_bar(img_stretched, "Histogram sau khi giãn biểu đồ")

plt.tight_layout()
plt.show()

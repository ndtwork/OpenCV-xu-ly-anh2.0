import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Đọc ảnh từ thư mục dự án
project_dir = os.path.dirname(os.path.dirname(__file__))  # Lấy thư mục dự án
image_path = os.path.join(project_dir, "Image_for_TeamSV", "FEMME-NOISE.png")
img = cv2.imread(image_path)

# Nếu ảnh là ảnh màu (3 kênh), chuyển nó sang ảnh xám
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thay X1 và X2 đều bằng img
X1 = img
X2 = img

# Tính và vẽ histogram dạng biểu đồ cột với cột rộng hơn
def plot_histogram_bar(image, title):
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))
    plt.bar(bin_edges[0:-1], histogram, color='blue', width=2)  # Đặt width=2 để làm rộng cột
    plt.title(title)
    plt.xlabel("Mức xám")
    plt.ylabel("Số lượng điểm ảnh")

# Tạo một figure duy nhất với layout hợp lý để vẽ tất cả đồ thị
plt.figure(figsize=(14, 10))

# Vẽ ảnh X1 và histogram X1
plt.subplot(3, 2, 1)
plt.imshow(X1, cmap='gray')
plt.title("Ảnh X1 (img) gốc")

plt.subplot(3, 2, 2)
plot_histogram_bar(X1, "Histogram (biểu đồ cột rộng) của X1 (img)")

# Vẽ ảnh X2 và histogram X2
plt.subplot(3, 2, 3)
plt.imshow(X2, cmap='gray')
plt.title("Ảnh X2 (img) gốc")

plt.subplot(3, 2, 4)
plot_histogram_bar(X2, "Histogram (biểu đồ cột rộng) của X2 (img)")

# Cân bằng histogram cho X2 (img)
X2_equalized = cv2.equalizeHist(X2.astype(np.uint8))

# Vẽ ảnh X2 sau khi cân bằng và histogram của nó
plt.subplot(3, 2, 5)
plt.imshow(X2_equalized, cmap='gray')
plt.title("Ảnh X2 sau khi cân bằng")

plt.subplot(3, 2, 6)
plot_histogram_bar(X2_equalized, "Histogram (biểu đồ cột rộng) của X2 sau khi cân bằng")

# Hiển thị tất cả đồ thị chỉ với một lần gọi plt.show()
plt.tight_layout()
plt.show()

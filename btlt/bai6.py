import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Đọc ảnh từ thư mục dự án
project_dir = os.path.dirname(os.path.dirname(__file__))  # Lấy thư mục dự án
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv2.imread(image_path)

# Nếu ảnh là ảnh màu (3 kênh), chuyển nó sang ảnh xám
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hàm hiển thị ảnh sau lọc
def plot_filtered_image(filtered_image, title):
    plt.imshow(filtered_image, cmap='gray')
    plt.title(title)
    plt.colorbar()

# Khởi tạo một hình để hiển thị kết quả
plt.figure(figsize=(10, 10))

# 1. Lọc thông thấp: Lọc trung bình
average_filter = cv2.blur(img, (3, 3))
plt.subplot(3, 3, 1)
plot_filtered_image(average_filter, "Lọc trung bình (3x3)")

# 2. Lọc thông thấp: Lọc Gaussian
gaussian_filter = cv2.GaussianBlur(img, (3, 3), 0)
plt.subplot(3, 3, 2)
plot_filtered_image(gaussian_filter, "Lọc Gaussian (3x3)")

# 3. Lọc thông cao: Lọc làm sắc nét
# Tạo một kernel lọc làm sắc nét
sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv2.filter2D(img, -1, sharpening_kernel)
plt.subplot(3, 3, 3)
plot_filtered_image(sharpened_image, "Lọc làm sắc nét")

# 4. Lọc đạo hàm: Lọc Sobel (X)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
plt.subplot(3, 3, 4)
plot_filtered_image(sobel_x, "Lọc Sobel X")

# 5. Lọc đạo hàm: Lọc Sobel (Y)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)
plt.subplot(3, 3, 5)
plot_filtered_image(sobel_y, "Lọc Sobel Y")

# 6. Lọc đạo hàm: Lọc Laplace
laplacian_filter = cv2.Laplacian(img, cv2.CV_64F)
laplacian_filter = cv2.convertScaleAbs(laplacian_filter)
plt.subplot(3, 3, 6)
plot_filtered_image(laplacian_filter, "Lọc Laplace")

plt.tight_layout()
plt.show()

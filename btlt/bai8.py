import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tạo ảnh nhị phân mẫu (hoặc đọc ảnh từ file)
img = np.zeros((100, 100), dtype="uint8")
cv2.rectangle(img, (30, 30), (70, 70), 255, -1)  # Tạo hình chữ nhật trắng trên nền đen

# Phần tử cấu trúc 3x3 hình vuông và dạng chữ thập
kernel_square = np.ones((3, 3), np.uint8)  # Phần tử 3x3 hình vuông
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # Phần tử chữ thập 3x3

# Áp dụng các phép toán hình thái học với kernel hình vuông
eroded_square = cv2.erode(img, kernel_square, iterations=1)
dilated_square = cv2.dilate(img, kernel_square, iterations=1)
closed_square = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_square)
opened_square = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_square)

# Áp dụng các phép toán hình thái học với kernel chữ thập
eroded_cross = cv2.erode(img, kernel_cross, iterations=1)
dilated_cross = cv2.dilate(img, kernel_cross, iterations=1)
closed_cross = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_cross)
opened_cross = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_cross)

# Hiển thị kết quả
plt.figure(figsize=(10, 8))

# Ảnh gốc
plt.subplot(3, 4, 1)
plt.imshow(img, cmap='gray')
plt.title("Ảnh gốc")

# Phép toán với kernel hình vuông
plt.subplot(3, 4, 2)
plt.imshow(eroded_square, cmap='gray')
plt.title("Co - Hình vuông")

plt.subplot(3, 4, 3)
plt.imshow(dilated_square, cmap='gray')
plt.title("Giãn - Hình vuông")

plt.subplot(3, 4, 4)
plt.imshow(closed_square, cmap='gray')
plt.title("Đóng - Hình vuông")

plt.subplot(3, 4, 5)
plt.imshow(opened_square, cmap='gray')
plt.title("Mở - Hình vuông")

# Phép toán với kernel chữ thập
plt.subplot(3, 4, 6)
plt.imshow(eroded_cross, cmap='gray')
plt.title("Co - Chữ thập")

plt.subplot(3, 4, 7)
plt.imshow(dilated_cross, cmap='gray')
plt.title("Giãn - Chữ thập")

plt.subplot(3, 4, 8)
plt.imshow(closed_cross, cmap='gray')
plt.title("Đóng - Chữ thập")

plt.subplot(3, 4, 9)
plt.imshow(opened_cross, cmap='gray')
plt.title("Mở - Chữ thập")

plt.tight_layout()
plt.show()

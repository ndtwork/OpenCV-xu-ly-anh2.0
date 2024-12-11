import cv2
import numpy as np
from linear_filters import high_pass_filter

# Đọc ảnh đầu vào (ảnh xám)
image = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng bộ lọc thông cao
high_pass_filtered = high_pass_filter(image)

# Áp dụng ngưỡng hóa để tạo ảnh nhị phân
_, binary_image = cv2.threshold(high_pass_filtered, 50, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh gốc, ảnh sau lọc thông cao, và ảnh nhị phân
cv2.imshow('Original Image', image)  # Hiển thị ảnh gốc
cv2.imshow('High Pass Filtered Image', high_pass_filtered)  # Hiển thị ảnh sau lọc
cv2.imshow('Binary Image', binary_image)  # Hiển thị ảnh nhị phân

# Chờ người dùng nhấn một phím để đóng cửa sổ hiển thị
cv2.waitKey(0)
cv2.destroyAllWindows()

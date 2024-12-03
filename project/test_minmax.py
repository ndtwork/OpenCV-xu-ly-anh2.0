import cv2
from nonlinear_filters import min_filter, max_filter

# Đọc ảnh đầu vào
image = cv2.imread('FEMME-NOISE.png', cv2.IMREAD_GRAYSCALE)

# Áp dụng lọc Min và Max
min_filtered_image = min_filter(image, kernel_size=5)
max_filtered_image = max_filter(image, kernel_size=5)

# Hiển thị kết quả
cv2.imshow('Original Image', image)
cv2.imshow('Min Filtered Image', min_filtered_image)
cv2.imshow('Max Filtered Image', max_filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

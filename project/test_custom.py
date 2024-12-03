import cv2
import numpy as np
import matplotlib.pyplot as plt

from custom_filters import custom_filter

# Ví dụ sử dụng
if __name__ == "__main__":
    # Đọc ảnh
    image = cv2.imread('car.jpg')  # Thay bằng đường dẫn ảnh của bạn
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Tạo kernel tùy chỉnh (ví dụ: kernel làm mờ trung bình)
    custom_kernel = np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]]) / 9  # Ma trận làm mờ 3x3

    # Áp dụng bộ lọc tùy chỉnh
    filtered_image_gray = custom_filter(image_gray, custom_kernel)
    filtered_image_color = custom_filter(image, custom_kernel)

    # Hiển thị ảnh
    plt.figure(figsize=(10, 5))

    # Ảnh gốc xám
    plt.subplot(1, 3, 1)
    plt.title("Original Grayscale")
    plt.imshow(image_gray, cmap='gray')
    plt.axis('off')

    # Ảnh lọc xám
    plt.subplot(1, 3, 2)
    plt.title("Filtered Grayscale")
    plt.imshow(filtered_image_gray, cmap='gray')
    plt.axis('off')

    # Ảnh lọc màu
    plt.subplot(1, 3, 3)
    plt.title("Filtered Color")
    plt.imshow(cv2.cvtColor(filtered_image_color, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.tight_layout()
    plt.show()

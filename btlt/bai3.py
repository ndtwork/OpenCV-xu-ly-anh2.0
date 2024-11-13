import numpy as np
import matplotlib.pyplot as plt
import cv2

# Ảnh gốc X1 và X2
X1 = np.array([
    [19, 17, 2, 1, 1, 2, 2, 1],
    [18, 19, 19, 17, 1, 1, 1, 1],
    [17, 18, 19, 17, 1, 2, 1, 1],
    [18, 19, 19, 19, 19, 1, 1, 2],
    [18, 19, 19, 18, 17, 2, 3, 3],
    [19, 19, 19, 18, 18, 2, 2, 1],
    [19, 19, 18, 18, 17, 1, 2, 1],
    [18, 19, 18, 17, 3, 1, 1, 3]
])

X2 = np.array([
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94]
])

# Hàm giãn tuyến tính
def linear_stretch(image):
    min_val, max_val = np.min(image), np.max(image)
    stretched = ((image - min_val) / (max_val - min_val)) * 255
    return stretched.astype(np.uint8)

# Hàm giãn với điểm ngưỡng
def threshold_stretch(image, lower_thresh=50, upper_thresh=200):
    stretched = np.copy(image)
    stretched[stretched < lower_thresh] = 0
    stretched[stretched > upper_thresh] = 255
    return stretched

# Hàm tuyến tính phân đoạn
def piecewise_linear(image, r1=50, s1=70, r2=150, s2=200):
    piecewise = np.piecewise(
        image,
        [image <= r1, (image > r1) & (image <= r2), image > r2],
        [lambda i: (s1 / r1) * i, 
         lambda i: ((s2 - s1) / (r2 - r1)) * (i - r1) + s1,
         lambda i: ((255 - s2) / (255 - r2)) * (i - r2) + s2]
    )
    return piecewise.astype(np.uint8)

# Áp dụng các phép biến đổi trên ảnh xám X1 và X2
X1_linear = linear_stretch(X1)
X1_threshold = threshold_stretch(X1)
X1_piecewise = piecewise_linear(X1)

X2_linear = linear_stretch(X2)
X2_threshold = threshold_stretch(X2)
X2_piecewise = piecewise_linear(X2)

# Hiển thị kết quả
plt.figure(figsize=(12, 8))

# Hiển thị kết quả cho X1
plt.subplot(3, 4, 1), plt.imshow(X1, cmap='gray'), plt.title('X1 Gốc')
plt.subplot(3, 4, 2), plt.imshow(X1_linear, cmap='gray'), plt.title('X1 Linear Stretch')
plt.subplot(3, 4, 3), plt.imshow(X1_threshold, cmap='gray'), plt.title('X1 Threshold Stretch')
plt.subplot(3, 4, 4), plt.imshow(X1_piecewise, cmap='gray'), plt.title('X1 Piecewise Linear')

# Hiển thị kết quả cho X2
plt.subplot(3, 4, 5), plt.imshow(X2, cmap='gray'), plt.title('X2 Gốc')
plt.subplot(3, 4, 6), plt.imshow(X2_linear, cmap='gray'), plt.title('X2 Linear Stretch')
plt.subplot(3, 4, 7), plt.imshow(X2_threshold, cmap='gray'), plt.title('X2 Threshold Stretch')
plt.subplot(3, 4, 8), plt.imshow(X2_piecewise, cmap='gray'), plt.title('X2 Piecewise Linear')

# Hiển thị ảnh màu giả lập và áp dụng biến đổi
X_color = np.stack([X2, X2, X2], axis=-1)  # Tạo ảnh màu từ X2
X_color_linear = linear_stretch(X_color)
X_color_threshold = threshold_stretch(X_color)
X_color_piecewise = piecewise_linear(X_color)

plt.subplot(3, 4, 9), plt.imshow(X_color), plt.title('Ảnh màu gốc')
plt.subplot(3, 4, 10), plt.imshow(X_color_linear), plt.title('Linear Stretch (Màu)')
plt.subplot(3, 4, 11), plt.imshow(X_color_threshold), plt.title('Threshold Stretch (Màu)')
plt.subplot(3, 4, 12), plt.imshow(X_color_piecewise), plt.title('Piecewise Linear (Màu)')

plt.tight_layout()
plt.show()

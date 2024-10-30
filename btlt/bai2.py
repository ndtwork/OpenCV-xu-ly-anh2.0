import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def adjust_gamma(image, gamma):
    # Chuyển đổi ảnh sang float32 để tính toán chính xác
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma for i in range(256)]).astype("float32")
    # Áp dụng biến đổi gamma
    return cv2.LUT(image, table)

# Đọc ảnh
project_dir = os.path.dirname(os.path.dirname(__file__))  # Lấy thư mục dự án
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv2.imread(image_path)

# Khảo sát các giá trị gamma
gamma_values = [0.5, 1.0, 2.0]  # Các giá trị gamma cần khảo sát
adjusted_images = []

# Áp dụng biến đổi gamma cho từng giá trị gamma
for gamma in gamma_values:
    adjusted = adjust_gamma(img, gamma)
    adjusted_images.append((gamma, adjusted))

# Hiển thị ảnh gốc và ảnh đã điều chỉnh
plt.figure(figsize=(10, 10))

# Hiển thị ảnh gốc
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Chuyển BGR sang RGB
plt.title('Ảnh gốc')

# Hiển thị ảnh đã điều chỉnh với các giá trị gamma
for i, (gamma, adjusted) in enumerate(adjusted_images):
    plt.subplot(2, 2, i + 2)
    plt.imshow(cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB))  # Chuyển BGR sang RGB
    plt.title(f'Gamma = {gamma}')

# Hiển thị hình ảnh
plt.tight_layout()
plt.show()

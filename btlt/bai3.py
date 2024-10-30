import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Hàm điều chỉnh Gamma
def adjust_gamma(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma for i in range(256)]).astype("float32")
    return cv2.LUT(image, table)

# Đọc ảnh gốc
project_dir = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img_color = cv2.imread(image_path)

# Chuyển đổi sang ảnh xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Giá trị gamma cần khảo sát
gamma_values = [0.5, 1.0, 2.0]

# Áp dụng biến đổi Gamma cho ảnh màu
adjusted_color_images = [(gamma, adjust_gamma(img_color, gamma)) for gamma in gamma_values]

# Áp dụng biến đổi Gamma cho ảnh xám
adjusted_gray_images = [(gamma, adjust_gamma(img_gray, gamma)) for gamma in gamma_values]

# Hiển thị ảnh gốc và các ảnh đã điều chỉnh
plt.figure(figsize=(12, 12))

# Hiển thị ảnh màu gốc
plt.subplot(3, 4, 1)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.title('Ảnh màu gốc')

# Hiển thị ảnh xám gốc
plt.subplot(3, 4, 5)
plt.imshow(img_gray, cmap='gray')
plt.title('Ảnh xám gốc')

# Hiển thị các ảnh màu sau khi biến đổi gamma
for i, (gamma, adjusted) in enumerate(adjusted_color_images):
    plt.subplot(3, 4, i + 2)
    plt.imshow(cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB))
    plt.title(f'Ảnh màu, Gamma = {gamma}')

# Hiển thị các ảnh xám sau khi biến đổi gamma
for i, (gamma, adjusted) in enumerate(adjusted_gray_images):
    plt.subplot(3, 4, i + 6)
    plt.imshow(adjusted, cmap='gray')
    plt.title(f'Ảnh xám, Gamma = {gamma}')

# Hiển thị toàn bộ
plt.tight_layout()
plt.show()

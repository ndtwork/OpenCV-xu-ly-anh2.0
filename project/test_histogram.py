import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_color_histogram(image):
    """
    Hiển thị histogram của 3 kênh màu (R, G, B) trong cùng một biểu đồ.
    Độ trong suốt alpha được tính theo công thức chuyển đổi sang grayscale.
    :param image: Ảnh đầu vào (numpy array, ảnh màu).
    """
    # Tách các kênh màu
    b, g, r = cv2.split(image)

    # Tính alpha cho mỗi kênh theo công thức chuyển đổi sang grayscale
    alpha_r = 0.299
    alpha_g = 0.587
    alpha_b = 0.114

    # Tạo histogram cho từng kênh
    plt.figure(figsize=(10, 5))
    plt.hist(r.ravel(), bins=256, range=(0, 256), color='red', alpha=alpha_r, label='Red')
    plt.hist(g.ravel(), bins=256, range=(0, 256), color='green', alpha=alpha_g, label='Green')
    plt.hist(b.ravel(), bins=256, range=(0, 256), color='blue', alpha=alpha_b, label='Blue')

    # Thiết lập biểu đồ
    plt.title("Color Histogram with Grayscale Alpha")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.show()



# Đọc ảnh màu
image = cv2.imread('car.jpg')  # Thay bằng đường dẫn ảnh của bạn
cv2.imshow('ảnh ô tô',image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển sang không gian màu RGB\

cv2.waitKey(0)
cv2.destroyAllWindows()
# Hiển thị histogram
plot_color_histogram(image)

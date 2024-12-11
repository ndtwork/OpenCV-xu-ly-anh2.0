import cv2
import numpy as np

"""Các bộ lọc thông thấp xóa nhiễu"""

def mean_filter(image, kernel_size=3):
    """
    Lọc thông thấp bằng mask lọc trung bình.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param kernel_size: Kích thước kernel (mặc định là 3x3).
    :return: Ảnh đã được lọc.
    """
    return cv2.blur(image, (kernel_size, kernel_size))


def gaussian_filter(image, kernel_size=3, sigma=1.0):
    """
    Lọc thông thấp bằng mask lọc Gauss.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param kernel_size: Kích thước kernel (mặc định là 3x3).
    :param sigma: Độ lệch chuẩn của phân phối Gauss (mặc định là 1.0).
    :return: Ảnh đã được lọc.
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX=sigma, sigmaY=sigma)


"""Bộ lọc thông cao (Smothing làm sắc nét)"""

def high_pass_filter(image):
    """
    Lọc thông cao (high-pass filter).
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :return: Ảnh đã được lọc thông cao.
    """
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)


"""Lọc đạo hàm"""

def sobel_filter(image, axis=2):
    """
    Lọc đạo hàm Sobel để phát hiện biên.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param axis: Trục đạo hàm (0: X-direction, 1: Y-direction, 2: Combined X and Y).
    :return: Ảnh đã áp dụng Sobel filter.
    """
    if axis == 0:
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X
    elif axis == 1:
        return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y
    elif axis == 2:
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
        return np.clip(sobel_combined, 0, 255).astype(np.uint8)
    else:
        raise ValueError("Axis must be 0 (X), 1 (Y), or 2 (Combined).")


def laplace_filter(image):
    """
    Lọc đạo hàm Laplace để phát hiện biên.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :return: Ảnh đã áp dụng Laplace filter.
    """
    return cv2.Laplacian(image, cv2.CV_64F, ksize=3)

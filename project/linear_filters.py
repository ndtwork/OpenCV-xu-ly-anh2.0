import numpy as np
from scipy.ndimage import convolve
import cv2


"""Các bộ lọc thông thấp xóa nhiễu"""
def mean_filter(image, kernel_size=3):
    """
    Lọc thông thấp bằng mask lọc trung bình.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param kernel_size: Kích thước kernel (mặc định là 3x3).
    :return: Ảnh đã được lọc.
    """
    if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
        # Tách các kênh BGR
        channels = cv2.split(image)
        filtered_channels = []

        # Áp dụng bộ lọc cho từng kênh
        for channel in channels:
            filtered_channel = convolve(channel, np.ones((kernel_size, kernel_size)) / (kernel_size ** 2))
            filtered_channels.append(filtered_channel)

        # Ghép các kênh đã lọc lại với nhau
        filtered_image = cv2.merge(filtered_channels)
    else:  # Nếu là ảnh xám (1 kênh)
        kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
        filtered_image = convolve(image, kernel)

    return filtered_image


def gaussian_filter(image, kernel_size=3, sigma=1.0):
    """
    Lọc thông thấp bằng mask lọc Gauss.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param kernel_size: Kích thước kernel (mặc định là 3x3).
    :param sigma: Độ lệch chuẩn của phân phối Gauss (mặc định là 1.0).
    :return: Ảnh đã được lọc.
    """
    if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
        # Tách các kênh BGR
        channels = cv2.split(image)
        filtered_channels = []

        # Áp dụng bộ lọc Gauss cho từng kênh
        for channel in channels:
            ax = np.linspace(-(kernel_size // 2), kernel_size // 2, kernel_size)
            gauss = np.exp(-0.5 * (ax / sigma) ** 2)
            gauss = gauss / np.sum(gauss)  # Chuẩn hóa để tổng kernel = 1
            kernel = np.outer(gauss, gauss)  # Tích outer để tạo kernel 2D

            filtered_channel = convolve(channel, kernel)
            filtered_channels.append(filtered_channel)

        # Ghép các kênh đã lọc lại với nhau
        filtered_image = cv2.merge(filtered_channels)

    else:  # Nếu là ảnh xám (1 kênh)
        ax = np.linspace(-(kernel_size // 2), kernel_size // 2, kernel_size)
        gauss = np.exp(-0.5 * (ax / sigma) ** 2)
        gauss = gauss / np.sum(gauss)  # Chuẩn hóa để tổng kernel = 1
        kernel = np.outer(gauss, gauss)  # Tích outer để tạo kernel 2D

        filtered_image = convolve(image, kernel)

    return filtered_image



"""Bộ lọc thông cao ( Smothing làm sắc nét)"""

def high_pass_filter(image):
    """
    Lọc thông cao (high-pass filter).
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :return: Ảnh đã được lọc thông cao.
    """
    # Kernel lọc thông cao (kết hợp bộ lọc edge detection)
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
        # Tách các kênh BGR
        channels = cv2.split(image)
        filtered_channels = []

        # Áp dụng bộ lọc cho từng kênh
        for channel in channels:
            filtered_channel = convolve(channel, kernel)
            filtered_channels.append(filtered_channel)

        # Ghép các kênh đã lọc lại với nhau
        filtered_image = cv2.merge(filtered_channels)
    else:  # Nếu là ảnh xám (1 kênh)
        filtered_image = convolve(image, kernel)

    return filtered_image


"""Lọc đạo hàm"""


def sobel_filter(image, axis=2):
    """
    Lọc đạo hàm Sobel để phát hiện biên.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param axis: Trục đạo hàm (0: X-direction, 1: Y-direction, 2: Combined X and Y).
    :return: Ảnh đã áp dụng Sobel filter.
    """
    # Kernel Sobel cho X và Y
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1],
                         [0,  0,  0],
                         [1,  2,  1]])

    if axis in [0, 1]:  # Đạo hàm riêng theo X hoặc Y
        kernel = kernel_x if axis == 0 else kernel_y
        if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
            channels = cv2.split(image)
            filtered_channels = []
            for channel in channels:
                filtered_channels.append(convolve(channel, kernel))
            filtered_image = cv2.merge(filtered_channels)
        else:  # Nếu là ảnh xám (1 kênh)
            filtered_image = convolve(image, kernel)
        return filtered_image

    elif axis == 2:  # Kết hợp cả X và Y
        if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
            channels = cv2.split(image)
            combined_channels = []
            for channel in channels:
                gx = convolve(channel, kernel_x)
                gy = convolve(channel, kernel_y)
                combined = np.sqrt(gx**2 + gy**2)
                combined_channels.append(combined)
            combined_image = cv2.merge(combined_channels)
        else:  # Nếu là ảnh xám (1 kênh)
            gx = convolve(image, kernel_x)
            gy = convolve(image, kernel_y)
            combined_image = np.clip(np.sqrt(gx**2 + gy**2), 0, 255).astype(np.uint8)

        # Chuẩn hóa kết quả về 0-255
        combined_image = np.clip(combined_image, 0, 255).astype(np.uint8)
        return combined_image

    else:
        raise ValueError("Axis must be 0 (X), 1 (Y), or 2 (Combined).")



def laplace_filter(image):
    """
    Lọc đạo hàm Laplace để phát hiện biên.
    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :return: Ảnh đã áp dụng Laplace filter.
    """
    # Kernel Laplace
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])

    if len(image.shape) == 3:  # Nếu là ảnh màu (3 kênh)
        channels = cv2.split(image)
        filtered_channels = []
        for channel in channels:
            filtered_channels.append(convolve(channel, kernel))
        filtered_image = cv2.merge(filtered_channels)
    else:  # Nếu là ảnh xám (1 kênh)
        filtered_image = convolve(image, kernel)

    return filtered_image

import cv2
import numpy as np


def median_filter(image, kernel_size=3):
    """
    Áp dụng lọc trung vị (Median Filter) lên ảnh.

    :param image: Ảnh đầu vào (mảng numpy 2D hoặc 3D).
    :param kernel_size: Kích thước của kernel (phải là số lẻ, ví dụ: 3, 5, 7,...).
    :return: Ảnh sau khi áp dụng lọc trung vị.
    """
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd number.")

    if len(image.shape) == 3:  # Nếu ảnh là ảnh màu
        channels = cv2.split(image)  # Tách kênh
        filtered_channels = []
        for channel in channels:
            filtered_channel = cv2.medianBlur(channel, kernel_size)  # Lọc trung vị trên từng kênh
            filtered_channels.append(filtered_channel)
        filtered_image = cv2.merge(filtered_channels)  # Ghép lại các kênh
    else:  # Nếu ảnh là ảnh xám
        filtered_image = cv2.medianBlur(image, kernel_size)

    return filtered_image


def min_filter(image, kernel_size=3):
    """
    Lọc Min để lấy giá trị nhỏ nhất trong vùng kernel.
    :param image: Ảnh đầu vào (numpy array, xám hoặc màu).
    :param kernel_size: Kích thước kernel (phải là số lẻ).
    :return: Ảnh sau khi áp dụng lọc Min.
    """
    # Tạo kernel
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Kiểm tra ảnh xám hay ảnh màu
    if len(image.shape) == 3:  # Ảnh màu
        channels = cv2.split(image)  # Tách các kênh màu
        min_filtered_channels = [cv2.erode(channel, kernel) for channel in channels]
        min_filtered = cv2.merge(min_filtered_channels)  # Ghép lại các kênh màu
    else:  # Ảnh xám
        min_filtered = cv2.erode(image, kernel)

    return min_filtered


def max_filter(image, kernel_size=3):
    """
    Lọc Max để lấy giá trị lớn nhất trong vùng kernel.
    :param image: Ảnh đầu vào (numpy array, xám hoặc màu).
    :param kernel_size: Kích thước kernel (phải là số lẻ).
    :return: Ảnh sau khi áp dụng lọc Max.
    """
    # Tạo kernel
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Kiểm tra ảnh xám hay ảnh màu
    if len(image.shape) == 3:  # Ảnh màu
        channels = cv2.split(image)  # Tách các kênh màu
        max_filtered_channels = [cv2.dilate(channel, kernel) for channel in channels]
        max_filtered = cv2.merge(max_filtered_channels)  # Ghép lại các kênh màu
    else:  # Ảnh xám
        max_filtered = cv2.dilate(image, kernel)

    return max_filtered

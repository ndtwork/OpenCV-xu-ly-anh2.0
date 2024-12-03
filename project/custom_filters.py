import cv2

def custom_filter(image, kernel):
    """
    Áp dụng bộ lọc tùy chỉnh lên ảnh.
    :param image: Ảnh đầu vào (numpy array, xám hoặc màu).
    :param kernel: Ma trận kernel tùy chỉnh (numpy array, kích thước lẻ, ví dụ: 3x3, 5x5).
    :return: Ảnh sau khi áp dụng bộ lọc.
    """
    # Kiểm tra kernel có kích thước lẻ hay không
    if kernel.shape[0] % 2 == 0 or kernel.shape[1] % 2 == 0:
        raise ValueError("Kernel size must be odd (e.g., 3x3, 5x5).")

    # Kiểm tra ảnh đầu vào
    if len(image.shape) == 3:  # Ảnh màu
        channels = cv2.split(image)
        filtered_channels = []
        for channel in channels:
            filtered_channel = cv2.filter2D(channel, -1, kernel)
            filtered_channels.append(filtered_channel)
        filtered_image = cv2.merge(filtered_channels)
    else:  # Ảnh xám
        filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

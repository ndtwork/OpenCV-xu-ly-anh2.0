import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Đường dẫn tới ảnh
    image_path = r"C:\Users\nguye\PycharmProjects\openCVtest2\notebook\car.jpg"

    # Đọc ảnh bằng OpenCV
    img_color = cv2.imread(image_path)   # hệ màu openCV mặc định là BGR

    gamma_value = 0.5  # Ví dụ: làm sáng ảnh
    img_color = apply_gamma_correction(img_color, gamma_value)

    # Kiểm tra xem ảnh có đọc được không
    if img_color is None:
        print("Không tìm thấy ảnh. Vui lòng kiểm tra lại đường dẫn:", image_path)
    else:

        # Chuyển ảnh từ BGR sang RGB để hiển thị đúng màu
        img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

        # Chuyển ảnh sang ảnh xám
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        # Tính histogram cho ảnh xám
        hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

        # Hiển thị ảnh gốc và ảnh xám
        plt.figure(figsize=(12, 12))

        # Hiển thị ảnh gốc (màu)
        plt.subplot(221)
        plt.imshow(img_rgb)
        plt.title('Ảnh gốc (Màu)')
        plt.axis('off')

        # Hiển thị ảnh xám
        plt.subplot(223)
        plt.imshow(img_gray, cmap='gray')
        plt.title('Ảnh xám')
        plt.axis('off')

        # Hiển thị histogram dạng cột
        plt.subplot(224)
        plt.bar(range(256), hist.ravel(), width=1, color='black')
        plt.title('Histogram (Ảnh xám)')
        plt.xlabel('Giá trị pixel')
        plt.ylabel('Số lượng pixel')
        plt.xlim([0, 256])


        # Tên các kênh và màu tương ứng
        channels = cv2.split(img_color)
        colors = ('blue', 'green', 'red')
        channel_names = ['Blue', 'Green', 'Red']

        plt.subplot(222)
        for channel, color, name in zip(channels, colors, channel_names):
            hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
            plt.plot(hist, color=color, label=f'Kênh {name}')
        plt.title('Histogram (Biểu đồ đường) cho 3 kênh màu')
        plt.xlabel('Giá trị pixel')
        plt.ylabel('Số lượng pixel')
        plt.legend()

        # Hiển thị tất cả
        plt.tight_layout()
        plt.show()


def apply_gamma_correction(image, gamma):
    """
    Hàm áp dụng gamma correction cho ảnh đầu vào.

    Args:
        image (numpy.ndarray): Ảnh đầu vào (BGR hoặc RGB).
        gamma (float): Giá trị gamma để chỉnh sửa.
                       Gamma > 1 làm sáng ảnh, gamma < 1 làm tối ảnh.

    Returns:
        numpy.ndarray: Ảnh sau khi áp dụng gamma correction.
    """
    # Kiểm tra ảnh đầu vào có hợp lệ
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ hoặc không tồn tại.")

    if gamma <= 0:
        raise ValueError("Gamma phải là một giá trị dương lớn hơn 0.")

    # Tạo bảng tra cứu giá trị pixel (LookUp Table - LUT)
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)]).astype("uint8")

    # Áp dụng bảng LUT lên ảnh
    corrected_image = cv2.LUT(image, table)
    return corrected_image


# Gọi hàm main()
if __name__ == "__main__":
    main()
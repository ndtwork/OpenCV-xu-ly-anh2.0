import cv2 as cv
import numpy as np

import os

project_dir = os.path.dirname(os.path.dirname(__file__))  # Get the project directory
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv.imread(image_path)

# Kiểm tra xem ảnh có được tải thành công không
if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra đường dẫn.")
else:
    # Chuyển đổi hệ màu từ RGB sang HSV
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Tạo một hình ảnh khác để sử dụng trong các phép toán
    img2 = np.zeros_like(img)
    img2[:, :] = [50, 100, 150]  # Màu RGB đơn giản

    # Sử dụng toán tử 'and'
    img_and = cv.bitwise_and(img, img2)

    # Sử dụng toán tử 'or'
    img_or = cv.bitwise_or(img, img2)

    # Sử dụng toán tử 'add'
    img_add = cv.add(img, img2)

    # Sử dụng toán tử 'sub'
    img_sub = cv.subtract(img, img2)

    # Hiển thị kết quả
    cv.imshow("Original Image", img)
    cv.imshow("AND Image", img_and)
    cv.imshow("OR Image", img_or)
    cv.imshow("Added Image", img_add)
    cv.imshow("Subtracted Image", img_sub)

    # Đợi phím bất kỳ để đóng cửa sổ
    cv.waitKey(0)
    cv.destroyAllWindows()

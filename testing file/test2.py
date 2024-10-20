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

    # Tính độ sáng trung bình
    mean_brightness = np.mean(img)

    # Kiểm tra nếu ảnh là âm bản hay dương bản dựa trên độ sáng trung bình
    if mean_brightness < 128:  # Giá trị giữa 0 và 255
        print("Ảnh có thể là âm bản.")
    else:
        print("Ảnh có thể là dương bản.")

    # Chuyển đổi hệ màu từ RGB sang HSV
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("HSV Image", hsv_img)

    # Chuyển đổi ảnh dương bản sang âm bản
    negative_img = 255 - img
    cv.imshow("Negative Image", negative_img)

    # Lưu ảnh âm bản ra file
    # cv.imwrite(r"C:\path_to_save\negative_car.jpg", negative_img)

    # Hiển thị ảnh gốc
    cv.imshow("Car Image", img)

    cv.waitKey(0)
    cv.destroyAllWindows()

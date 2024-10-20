import cv2
import cv2 as cv

import os

project_dir = os.path.dirname(os.path.dirname(__file__))  # Get the project directory
image_path = os.path.join(project_dir, "Image_for_TeamSV", "car.jpg")
img = cv.imread(image_path)

# Kiểm tra nếu ảnh được đọc thành công
if img is None:
    print("Không thể đọc file ảnh.")
else:
    # Độ phân giải (chiều rộng x chiều cao)
    height, width, channels = img.shape
    print(f"Độ phân giải: {width} x {height}")

    # Độ sâu (số bit trên mỗi kênh màu)
    depth = img.dtype
    print(f"Độ sâu màu: {depth} (loại dữ liệu)")

    # Tổng số kênh màu (ví dụ: RGB có 3 kênh)
    print(f"Số kênh màu: {channels}")

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    resized_img = cv.resize(img, (400, 100))
    # lam mo anh
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    # phat hien canh
    edges = cv2.Canny(img, 100, 200)
    # anh nhi phan
    ret, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #
    # contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    # Tạo ảnh âm bản
    negative_image = cv2.bitwise_not(img)

    # Hiển thị ảnh gốc và ảnh âm bản
    cv2.imshow('Original Image', img)
    cv2.imshow('Negative Image', negative_image)

    # cv.imshow("Display window", binary_img)
    k = cv.waitKey(0)  # Wait for a keystroke in the window
    cv2.destroyAllWindows()






# cv2.imread(): Đọc ảnh từ tệp.
# cv2.imwrite(): Lưu ảnh xuống ổ đĩa.
# cv2.imshow(): Hiển thị ảnh trong cửa sổ.
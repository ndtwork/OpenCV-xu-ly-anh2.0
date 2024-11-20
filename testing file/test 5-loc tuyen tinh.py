import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, gaussian_filter
import os

# Get the project directory and image path
project_dir = os.path.dirname(os.path.dirname(__file__))
image_path = os.path.join(project_dir, "Image_for_TeamSV", "FEMME-NOISE.png")

# Read the image
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra đường dẫn.")
else:
    # Average filter
    average_filter = np.ones((3, 3)) / 9
    img_average_filtered = convolve(img, average_filter)

    # Gaussian filter
    img_gaussian_filtered = gaussian_filter(img, sigma=1)

    # Sharpening filter
    sharpening_filter = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    img_sharpened = convolve(img, sharpening_filter)

    # Display original and filtered images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Ảnh gốc')

    plt.subplot(1, 4, 2)
    plt.imshow(img_average_filtered, cmap='gray')
    plt.title('Lọc trung bình')

    plt.subplot(1, 4, 3)
    plt.imshow(img_gaussian_filtered, cmap='gray')
    plt.title('Lọc Gaussian')

    plt.subplot(1, 4, 4)
    plt.imshow(img_sharpened, cmap='gray')
    plt.title('Lọc làm sắc nét')

    plt.tight_layout()
    plt.show()

    # Display histograms
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.hist(img.ravel(), bins=256, range=(0, 255), color='gray')
    plt.title('Histogram ảnh gốc')
    plt.xlabel('Mức xám')
    plt.ylabel('Số lượng pixel')

    plt.subplot(1, 4, 2)
    plt.hist(img_average_filtered.ravel(), bins=256, range=(0, 255), color='gray')
    plt.title('Histogram lọc trung bình')
    plt.xlabel('Mức xám')
    plt.ylabel('Số lượng pixel')

    plt.subplot(1, 4, 3)
    plt.hist(img_gaussian_filtered.ravel(), bins=256, range=(0, 255), color='gray')
    plt.title('Histogram lọc Gaussian')
    plt.xlabel('Mức xám')
    plt.ylabel('Số lượng pixel')

    plt.subplot(1, 4, 4)
    plt.hist(img_sharpened.ravel(), bins=256, range=(0, 255), color='gray')
    plt.title('Histogram lọc làm sắc nét')
    plt.xlabel('Mức xám')
    plt.ylabel('Số lượng pixel')

    plt.tight_layout()
    plt.show()
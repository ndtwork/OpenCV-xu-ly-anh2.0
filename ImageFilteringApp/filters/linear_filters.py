import numpy as np
from scipy.ndimage import convolve

def low_pass_filter(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    return convolve(image, kernel)

def high_pass_filter(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
    return convolve(image, kernel)

def combined_filter(image):
    low = low_pass_filter(image)
    high = high_pass_filter(image)
    return low + high

def derivative_filter(image, axis=0):
    if axis == 0:  # X-direction
        kernel = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
    elif axis == 1:  # Y-direction
        kernel = np.array([[-1, -2, -1],
                           [0,  0,  0],
                           [1,  2,  1]])
    else:
        raise ValueError("Axis must be 0 (X) or 1 (Y).")
    return convolve(image, kernel)

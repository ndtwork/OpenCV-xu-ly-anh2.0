import numpy as np
from scipy.ndimage import minimum_filter, maximum_filter, median_filter

def median_filtering(image, size=3):
    return median_filter(image, size=size)

def min_filter(image, size=3):
    return minimum_filter(image, size=size)

def max_filter(image, size=3):
    return maximum_filter(image, size=size)

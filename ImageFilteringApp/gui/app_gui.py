import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
from filters.linear_filters import low_pass_filter, high_pass_filter, combined_filter, derivative_filter
from filters.nonlinear_filters import median_filtering, min_filter, max_filter


class ImageFilteringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filtering App")

        # Elements
        self.image_label = tk.Label(self.root, text="No Image Loaded")
        self.image_label.pack()

        self.filter_type = tk.StringVar(value="linear")
        filter_options = ttk.Combobox(self.root, textvariable=self.filter_type, values=["linear", "nonlinear"])
        filter_options.pack()

        self.apply_button = tk.Button(self.root, text="Apply Filter", command=self.apply_filter)
        self.apply_button.pack()

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.save_button = tk.Button(self.root, text="Save Output", command=self.save_image)
        self.save_button.pack()

        self.image = None
        self.filtered_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.image = image
            self.display_image(image)

    def display_image(self, image):
        im = Image.fromarray((image * 255 / np.max(image)).astype(np.uint8)) if image.max() > 1 else Image.fromarray(
            image)
        im_tk = ImageTk.PhotoImage(im)
        self.image_label.config(image=im_tk)
        self.image_label.image = im_tk

    def apply_filter(self):
        if self.image is None:
            return

        if self.filter_type.get() == "linear":
            self.filtered_image = low_pass_filter(self.image)  # Chọn lọc tuyến tính
        elif self.filter_type.get() == "nonlinear":
            self.filtered_image = median_filtering(self.image)  # Chọn lọc phi tuyến

        if self.filtered_image is not None:
            self.display_image(self.filtered_image)

    def save_image(self):
        if self.filtered_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.filtered_image)


def run():
    root = tk.Tk()
    app = ImageFilteringApp(root)
    root.mainloop()

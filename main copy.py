import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QFileDialog, QAction, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog
import cv2
# Import linear filters
from project.linear_filters import (
    mean_filter, gaussian_filter, high_pass_filter, sobel_filter, laplace_filter
)
from project.nonlinear_filters import (
    median_filter, min_filter, max_filter
)


class ImageFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1400, 800)
        self.setWindowTitle("Image Filter Application")
        self.image = None  # Store the imported image

        # Main Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Top Layout
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        # Original Image Box
        self.original_label_title = QLabel("Original Image")
        self.original_label_title.setAlignment(Qt.AlignCenter)
        self.original_label = QLabel(self)
        self.original_label.setStyleSheet("border: 1px solid black; background-color: white;")
        self.original_label.setScaledContents(True)
        self.top_layout.addWidget(self.create_image_box("Original Image", self.original_label))

        # Filtered Image Box
        self.filtered_label_title = QLabel("Filtered Image")
        self.filtered_label_title.setAlignment(Qt.AlignCenter)
        self.filtered_label = QLabel(self)
        self.filtered_label.setStyleSheet("border: 1px solid black; background-color: white;")
        self.filtered_label.setScaledContents(True)
        self.top_layout.addWidget(self.create_image_box("Filtered Image", self.filtered_label))

        # Bottom Layout for Histogram
        self.histogram_view = QChartView()
        self.histogram_view.setRenderHint(QPainter.Antialiasing)
        self.main_layout.addWidget(self.histogram_view)

        # Create Menu Bar
        self.create_menu_bar()

    def create_image_box(self, title: str, label: QLabel) -> QWidget:
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        layout.addWidget(label)
        box_widget = QWidget()
        box_widget.setLayout(layout)
        return box_widget

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Import Image", self)
        open_action.triggered.connect(self.load_image)
        file_menu.addAction(open_action)

        clear_action = QAction("Clear Images", self)
        clear_action.triggered.connect(self.clear_images)
        file_menu.addAction(clear_action)

        save_action = QAction("Save Filtered Image", self)
        save_action.triggered.connect(self.save_filtered_image)
        file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Linear Filters Menu
        linear_menu = menu_bar.addMenu("Linear Filters")
        mean_action = QAction("Mean Filter", self)
        mean_action.triggered.connect(self.apply_mean_filter)
        linear_menu.addAction(mean_action)

        gaussian_action = QAction("Gaussian Filter", self)
        gaussian_action.triggered.connect(self.apply_gaussian_filter)
        linear_menu.addAction(gaussian_action)

        high_pass_action = QAction("High Pass Filter", self)
        high_pass_action.triggered.connect(self.apply_high_pass_filter)
        linear_menu.addAction(high_pass_action)

        sobel_action = QAction("Sobel Filter", self)
        sobel_action.triggered.connect(self.apply_sobel_filter)
        linear_menu.addAction(sobel_action)

        laplace_action = QAction("Laplace Filter", self)
        laplace_action.triggered.connect(self.apply_laplace_filter)
        linear_menu.addAction(laplace_action)

        # Non-linear Filters Menu
        non_linear_menu = menu_bar.addMenu("Non-linear Filters")
        median_action = QAction("Median Filter", self)
        median_action.triggered.connect(self.apply_median_filter)
        non_linear_menu.addAction(median_action)

        min_action = QAction("Min Filter", self)
        min_action.triggered.connect(self.apply_min_filter)
        non_linear_menu.addAction(min_action)

        max_action = QAction("Max Filter", self)
        max_action.triggered.connect(self.apply_max_filter)
        non_linear_menu.addAction(max_action)

        # Additional Non-filter Functionality
        non_filter_action = QAction("Non-filter Operation", self)
        non_filter_action.triggered.connect(self.non_filter_operation)
        non_linear_menu.addAction(non_filter_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            self.image = QImage(file_path)
            if self.image.isNull():
                QMessageBox.warning(self, "Error", "Failed to load image.")
            else:
                pixmap = QPixmap.fromImage(self.image)
                self.display_image(self.original_label, pixmap)

    def display_image(self, label, pixmap):
        max_width, max_height = 600, 600
        if pixmap.width() > max_width or pixmap.height() > max_height:
            pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())

    def save_filtered_image(self):
        if not self.filtered_label.pixmap():
            QMessageBox.warning(self, "Error", "No filtered image to save!")
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Filtered Image", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            self.filtered_label.pixmap().save(file_path)

    def clear_images(self):
        self.original_label.clear()
        self.filtered_label.clear()
        self.histogram_view.setChart(None)

    def apply_mean_filter(self):
        self.apply_external_filter(mean_filter, "Mean Filter Applied")

    def apply_gaussian_filter(self):
        self.apply_external_filter(gaussian_filter, "Gaussian Filter Applied", kernel_size=3, sigma=1.0)

    def apply_high_pass_filter(self):
        self.apply_external_filter(high_pass_filter, "High Pass Filter Applied")

    def apply_sobel_filter(self):
        self.apply_external_filter(sobel_filter, "Sobel Filter Applied")

    def apply_laplace_filter(self):
        self.apply_external_filter(laplace_filter, "Laplace Filter Applied")

    def apply_external_filter(self, filter_func, success_message, **kwargs):
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        array = self.qimage_to_array(self.image)
        filtered_array = filter_func(array, **kwargs)
        self.display_filtered_image(filtered_array, success_message)

    # def apply_median_filter(self):
    #     self.apply_non_linear_filter(median_filter, "Median Filter Applied")

    def apply_median_filter(self):
        """Prompt for kernel size and apply the median filter."""
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        
        # Prompt user for kernel size
        kernel_size, ok = QInputDialog.getInt(self, "Kernel Size", "Enter kernel size (odd number):", min=3, max=21, step=2)
        if ok:
            array = self.qimage_to_array(self.image)
            filtered_array = self.apply_median_filter_logic(array, kernel_size)
            self.display_filtered_image(filtered_array, "Median Filter Applied")

    def apply_median_filter_logic(self, image, kernel_size):
        """Apply a median filter to the image."""
        # Convert to grayscale if the image is in color
        if len(image.shape) == 3:  # Color image (3 channels)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = image

        # Ensure the image is of type uint8
        gray_image = np.uint8(gray_image)

        # Apply the median filter
        filtered_image = cv2.medianBlur(gray_image, kernel_size)
        
        return filtered_image


    def apply_min_filter(self):
        self.apply_non_linear_filter(min_filter, "Min Filter Applied")

    def apply_max_filter(self):
        self.apply_non_linear_filter(max_filter, "Max Filter Applied")

    def apply_non_linear_filter(self, filter_func, success_message):
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        array = self.qimage_to_array(self.image)
        gray_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        filtered_array = filter_func(gray_array)
        self.display_filtered_image(filtered_array, success_message)

    def non_filter_operation(self):
        # This is a placeholder for any non-filter operation you want to add.
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        # Example non-filter operation (just inverting the colors)
        array = self.qimage_to_array(self.image)
        inverted_array = 255 - array  # Invert the image colors
        self.display_filtered_image(inverted_array, "Non-filter Operation Applied")

    def display_filtered_image(self, filtered_array, success_message):
        filtered_image = self.array_to_qimage(filtered_array)
        pixmap = QPixmap.fromImage(filtered_image)
        self.display_image(self.filtered_label, pixmap)
        self.show_histogram(filtered_array)
        QMessageBox.information(self, "Success", success_message)

    def show_histogram(self, array):
        """Show the histogram of the image."""
        hist, _ = np.histogram(array.flatten(), bins=256, range=[0, 256])
        chart = QChart()
        bar_set = QBarSet("Histogram")
        bar_set.append(hist)
        series = QBarSeries()
        series.append(bar_set)
        chart.addSeries(series)
        axis = QBarCategoryAxis()
        axis.append([str(i) for i in range(256)])
        chart.setAxisX(axis, series)
        chart.setAxisY(axis, series)
        self.histogram_view.setChart(chart)

    def qimage_to_array(self, qimage):
        """Convert a QImage to a numpy array."""
        if qimage.isNull():
            return None
        raw_data = qimage.bits().asstring(qimage.byteCount())
        arr = np.frombuffer(raw_data, dtype=np.uint8).reshape((qimage.height(), qimage.width(), 4))
        return arr[..., :3]  # Ignore the alpha channel for now

    # def array_to_qimage(self, arr):
    #     """Convert a numpy array to QImage."""
    #     h, w = arr.shape
    #     return QImage(arr.data, w, h, 3 * w, QImage.Format_RGB888)

    def array_to_qimage(self, arr):
        """Convert a numpy array to QImage."""
        if arr.ndim == 3:  # Color image (RGB or RGBA)
            h, w, c = arr.shape
            if c == 3:  # RGB
                return QImage(arr.data, w, h, 3 * w, QImage.Format_RGB888)
            elif c == 4:  # RGBA
                return QImage(arr.data, w, h, 4 * w, QImage.Format_ARGB32)
        elif arr.ndim == 2:  # Grayscale image
            h, w = arr.shape
            return QImage(arr.data, w, h, w, QImage.Format_Grayscale8)
        else:
            raise ValueError("Unsupported array shape: {}".format(arr.shape))

    def show_about(self):
        """Display the 'About' information."""
        QMessageBox.about(self, "About", "This is an image filter application built with PyQt5.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec_())

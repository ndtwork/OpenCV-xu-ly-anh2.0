import sys
import numpy as np
from scipy.ndimage import convolve, median_filter, minimum_filter, maximum_filter
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QFileDialog, QAction, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtCore import Qt


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
        self.top_layout.addWidget(self.create_image_box(self.original_label_title, self.original_label))

        # Filtered Image Box
        self.filtered_label_title = QLabel("Filtered Image")
        self.filtered_label_title.setAlignment(Qt.AlignCenter)
        self.filtered_label = QLabel(self)
        self.filtered_label.setStyleSheet("border: 1px solid black; background-color: white;")
        self.filtered_label.setScaledContents(True)
        self.top_layout.addWidget(self.create_image_box(self.filtered_label_title, self.filtered_label))

        # Bottom Layout
        self.bottom_widget = QLabel("Graph will display here.")
        self.bottom_widget.setAlignment(Qt.AlignCenter)
        self.bottom_widget.setFixedHeight(200)
        self.bottom_widget.setStyleSheet("border: 1px solid black; background-color: lightgray;")
        self.main_layout.addWidget(self.bottom_widget)

        # Create Menu Bar
        self.create_menu_bar()

    def create_image_box(self, title: str, label: QLabel) -> QWidget:
        """
        Creates a widget containing a title and a label for displaying an image.
        """
        # Create a vertical layout for the title and label
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        layout.addWidget(label)

        # Create a QWidget to encapsulate the layout
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

        # Linear Filters menu
        linear_menu = menu_bar.addMenu("Linear Filters")
        low_pass_action = QAction("Low Pass Filter", self)
        low_pass_action.triggered.connect(self.apply_low_pass_filter)
        linear_menu.addAction(low_pass_action)

        high_pass_action = QAction("High Pass Filter", self)
        high_pass_action.triggered.connect(self.apply_high_pass_filter)
        linear_menu.addAction(high_pass_action)

        median_action = QAction("Median Filter", self)
        median_action.triggered.connect(self.apply_median_filter)
        linear_menu.addAction(median_action)

        combined_action = QAction("Combined Filter", self)
        combined_action.triggered.connect(self.apply_combined_filter)
        linear_menu.addAction(combined_action)

        derivative_action = QAction("Derivative Filter", self)
        derivative_action.triggered.connect(self.apply_derivative_filter)
        linear_menu.addAction(derivative_action)

        # Non-linear Filters menu
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
        # Resize QLabel to fit the image or scale down if the image is too large
        max_width, max_height = 600, 600
        image_width, image_height = pixmap.width(), pixmap.height()

        if image_width > max_width or image_height > max_height:
            pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)

        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())

    def save_filtered_image(self):
        if not self.filtered_label.pixmap():
            QMessageBox.warning(self, "Error", "No filtered image to save!")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Filtered Image", "", "Images (*.png *.jpg *.bmp *.jpeg)"
        )
        if file_path:
            self.filtered_label.pixmap().save(file_path)

    def clear_images(self):
        self.original_label.clear()
        self.filtered_label.clear()
        self.bottom_widget.setText("Graph will display here.")

    def apply_low_pass_filter(self):
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        self.apply_filter(np.ones((3, 3)) / 9, "Low-Pass Filter Applied")

    def apply_high_pass_filter(self):
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        self.apply_filter(kernel, "High-Pass Filter Applied")

    def apply_median_filter(self):
        if not self.image:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        array = self.qimage_to_array(self.image)
        gray_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        filtered_array = median_filter(gray_array, size=3)
        self.display_filtered_image(filtered_array, "Median Filter Applied")

    def apply_combined_filter(self):
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        self.apply_filter(kernel=kernel)

    def apply_derivative_filter(self):
        kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        self.apply_filter(kernel=kernel)

    def apply_min_filter(self):
        self.apply_filter(non_linear_fn=lambda x: minimum_filter(x, size=3))

    def apply_max_filter(self):
        self.apply_filter(non_linear_fn=lambda x: maximum_filter(x, size=3))

    def apply_filter(self, kernel, success_message):
        array = self.qimage_to_array(self.image)
        gray_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        filtered_array = convolve(gray_array, kernel, mode='constant', cval=0.0)
        self.display_filtered_image(filtered_array, success_message)

    def display_filtered_image(self, filtered_array, success_message):
        filtered_qimage = self.array_to_qimage(filtered_array)
        pixmap = QPixmap.fromImage(filtered_qimage)
        self.display_image(self.filtered_label, pixmap)
        self.bottom_widget.setText(success_message)

    def show_about(self):
        QMessageBox.information(self, "About", "This application applies image filters (linear and non-linear).")

    def qimage_to_array(self, image):
        width = image.width()
        height = image.height()
        bytes_per_line = image.bytesPerLine()
        format_ = image.format()

        if format_ not in (QImage.Format_RGB32, QImage.Format_ARGB32, QImage.Format_ARGB32_Premultiplied):
            image = image.convertToFormat(QImage.Format_RGB32)

        ptr = image.bits()
        ptr.setsize(bytes_per_line * height)
        array = np.array(ptr).reshape((height, bytes_per_line // 4, 4))
        return array[:, :, :3]  # Extract RGB

    def array_to_qimage(self, array):
        array = np.clip(array, 0, 255).astype(np.uint8)
        return QImage(array.data, array.shape[1], array.shape[0], array.shape[1], QImage.Format_Grayscale8)


def main():
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec_())


main()

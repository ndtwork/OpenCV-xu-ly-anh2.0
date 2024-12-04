import sys
import numpy as np
from scipy.ndimage import convolve, median_filter, minimum_filter, maximum_filter
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QFileDialog, QAction, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget,
    QDialog, QLineEdit, QGridLayout, QPushButton, QInputDialog
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class CustomFilterDialog(QDialog):
    def __init__(self, parent=None, size=3):
        super().__init__(parent)
        self.size = size
        self.setWindowTitle(f"Custom {size}x{size} Filter")
        self.entries = []

        self.layout = QGridLayout(self)

        # Create input grid for the filter values
        for i in range(size):
            row = []
            for j in range(size):
                entry = QLineEdit(self)
                entry.setPlaceholderText(f"({i+1},{j+1})")
                self.layout.addWidget(entry, i, j)
                row.append(entry)
            self.entries.append(row)

        # Add Apply button
        self.apply_button = QPushButton("Apply Filter", self)
        self.apply_button.clicked.connect(self.apply_filter)
        self.layout.addWidget(self.apply_button, size, 0, 1, size)

    def apply_filter(self):
        try:
            # Convert user input to a numeric numpy array
            custom_filter = np.array([[eval(entry.text()) for entry in row] for row in self.entries])
            self.parent().apply_custom_filter(custom_filter)
            self.accept()
        except Exception:
            QMessageBox.warning(self, "Error", "Invalid input! Please enter valid numbers or fractions.")


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
        self.top_layout.addWidget(self.create_image_box(self.original_label_title, self.original_label))

        # Filtered Image Box
        self.filtered_label_title = QLabel("Filtered Image")
        self.filtered_label_title.setAlignment(Qt.AlignCenter)
        self.filtered_label = QLabel(self)
        self.filtered_label.setStyleSheet("border: 1px solid black; background-color: white;")
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

        linear_menu = menu_bar.addMenu("Linear Filters")
        low_pass_action = QAction("Low Pass Filter", self)
        low_pass_action.triggered.connect(self.apply_low_pass_filter)
        linear_menu.addAction(low_pass_action)

        high_pass_action = QAction("High Pass Filter", self)
        high_pass_action.triggered.connect(self.apply_high_pass_filter)
        linear_menu.addAction(high_pass_action)

        derivative_action = QAction("Derivative Filter", self)
        derivative_action.triggered.connect(self.apply_derivative_filter)
        linear_menu.addAction(derivative_action)

        custom_filter_action = QAction("Custom Filter", self)
        custom_filter_action.triggered.connect(self.open_custom_filter_dialog)
        linear_menu.addAction(custom_filter_action)

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
                self.original_label.setPixmap(pixmap)

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
        self.bottom_widget.setText("Graph will display here.")

    def open_custom_filter_dialog(self):
        size, ok = QInputDialog.getItem(self, "Select Filter Size", "Choose filter size:", ["3x3", "5x5"], 0, False)
        if ok:
            size = 3 if size == "3x3" else 5
            dialog = CustomFilterDialog(self, size)
            dialog.exec_()

    def apply_custom_filter(self, custom_filter):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        gray_image = self.qimage_to_gray_array(self.image)
        filtered_array = convolve(gray_image, custom_filter, mode='constant', cval=0.0)
        self.display_filtered_image(filtered_array, "Custom Filter Applied")

    def apply_low_pass_filter(self):
        kernel = np.ones((3, 3)) / 9
        self.apply_filter(kernel, "Low-Pass Filter Applied")

    def apply_high_pass_filter(self):
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        self.apply_filter(kernel, "High-Pass Filter Applied")

    def apply_derivative_filter(self):
        kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        self.apply_filter(kernel, "Derivative Filter Applied")

    def apply_median_filter(self):
        self.apply_non_linear_filter(lambda x: median_filter(x, size=3), "Median Filter Applied")

    def apply_min_filter(self):
        self.apply_non_linear_filter(lambda x: minimum_filter(x, size=3), "Min Filter Applied")

    def apply_max_filter(self):
        self.apply_non_linear_filter(lambda x: maximum_filter(x, size=3), "Max Filter Applied")

    def apply_filter(self, kernel, message):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        gray_image = self.qimage_to_gray_array(self.image)
        filtered_array = convolve(gray_image, kernel, mode='constant', cval=0.0)
        self.display_filtered_image(filtered_array, message)

    def apply_non_linear_filter(self, func, message):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return
        gray_image = self.qimage_to_gray_array(self.image)
        filtered_array = func(gray_image)
        self.display_filtered_image(filtered_array, message)

    def display_filtered_image(self, filtered_array, message):
        filtered_qimage = self.array_to_qimage(filtered_array)
        pixmap = QPixmap.fromImage(filtered_qimage)
        self.filtered_label.setPixmap(pixmap)
        self.bottom_widget.setText(message)

    def qimage_to_gray_array(self, image):
        ptr = image.bits()
        ptr.setsize(image.bytesPerLine() * image.height())
        arr = np.array(ptr).reshape((image.height(), image.bytesPerLine() // 4, 4))
        return np.dot(arr[..., :3], [0.2989, 0.5870, 0.1140])

    def array_to_qimage(self, array):
        array = np.clip(array, 0, 255).astype(np.uint8)
        height, width = array.shape
        return QImage(array.data, width, height, QImage.Format_Grayscale8)

    def show_about(self):
        QMessageBox.information(self, "About", "This application applies various image filters.")


def main():
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

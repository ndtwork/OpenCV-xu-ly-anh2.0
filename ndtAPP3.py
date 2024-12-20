import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QFileDialog, QAction, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget,
    QDialog, QGridLayout, QLineEdit, QPushButton, QComboBox, QWidgetAction
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class MultiFilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Multi-Filters")
        self.filters = []  # Store all custom filters
        self.current_filter_index = 0
        self.size = 3  # Default filter size is 3x3

        self.layout = QVBoxLayout(self)

        # Step 1: Input number of filters
        self.step1_label = QLabel("Enter the number of filters:")
        self.layout.addWidget(self.step1_label)

        self.num_filters_input = QLineEdit(self)
        self.num_filters_input.setPlaceholderText("Number of filters (e.g., 2)")
        self.layout.addWidget(self.num_filters_input)

        # Step 2: Dynamic filter input
        self.filter_grid = QGridLayout()
        self.filter_entries = []  # To store QLineEdit for one filter
        self.layout.addLayout(self.filter_grid)

        # Add buttons
        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_step)
        self.layout.addWidget(self.next_button)

        self.apply_button = QPushButton("Apply All Filters", self)
        self.apply_button.clicked.connect(self.apply_all_filters)
        self.layout.addWidget(self.apply_button)
        self.apply_button.hide()  # Only show after all filters are entered

    def next_step(self):
        if self.current_filter_index == 0:  # Step 1: Set number of filters
            try:
                num_filters = int(self.num_filters_input.text())
                if num_filters <= 0:
                    raise ValueError
                self.num_filters = num_filters
                self.filters = []
                self.current_filter_index = 1
                self.step1_label.setText(f"Enter Filter 1 (size: {self.size}x{self.size}):")
                self.num_filters_input.hide()
                self.create_filter_grid()
            except ValueError:
                QMessageBox.warning(self, "Error", "Please enter a valid number greater than 0.")
        else:  # Step 2: Collect filter values
            try:
                filter_values = np.array([
                    [float(entry.text()) for entry in row]
                    for row in self.filter_entries
                ])
                self.filters.append(filter_values)
                if len(self.filters) < self.num_filters:
                    self.step1_label.setText(f"Enter Filter {len(self.filters) + 1} (size: {self.size}x{self.size}):")
                    self.create_filter_grid()
                else:
                    self.step1_label.setText(f"All {self.num_filters} filters are entered.")
                    self.filter_grid.deleteLater()
                    self.next_button.hide()
                    self.apply_button.show()
            except Exception:
                QMessageBox.warning(self, "Error", "Invalid filter values! Please enter numbers.")

    def create_filter_grid(self):
        # Reset grid layout
        for i in reversed(range(self.filter_grid.count())):
            self.filter_grid.itemAt(i).widget().setParent(None)

        self.filter_entries = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                entry = QLineEdit(self)
                entry.setPlaceholderText(f"({i + 1},{j + 1})")
                self.filter_grid.addWidget(entry, i, j)
                row.append(entry)
            self.filter_entries.append(row)

    def apply_all_filters(self):
        self.parent().apply_custom_multi_filters(self.filters)
        self.accept()


class ImageFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1400, 800)
        self.setWindowTitle("Image Filter Application")
        self.image = None  # Store the imported image
        self.filter_size = 3  # Default filter size is 3x3

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

        # File menu
        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Import Image", self)
        open_action.triggered.connect(self.load_image)
        file_menu.addAction(open_action)

        save_action = QAction("Save Filtered Image", self)
        save_action.triggered.connect(self.save_filtered_image)
        file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Linear Filters menu
        linear_menu = menu_bar.addMenu("Linear Filters")

        # Add QComboBox to menu as a widget
        filter_size_action = QAction("Filter Size", self)
        filter_size_action.setDisabled(True)
        linear_menu.addAction(filter_size_action)

        self.filter_size_combo = QComboBox(self)
        self.filter_size_combo.addItems(["3x3", "5x5"])
        self.filter_size_combo.currentIndexChanged.connect(self.change_filter_size)

        widget_action = QWidgetAction(self)
        widget_action.setDefaultWidget(self.filter_size_combo)
        linear_menu.addAction(widget_action)

        low_pass_action = QAction("Low Pass Filter", self)
        low_pass_action.triggered.connect(self.apply_low_pass_filter)
        linear_menu.addAction(low_pass_action)

        high_pass_action = QAction("High Pass Filter", self)
        high_pass_action.triggered.connect(self.apply_high_pass_filter)
        linear_menu.addAction(high_pass_action)

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

        # Custom Filters menu
        custom_menu = menu_bar.addMenu("Custom Filters")
        multi_filter_action = QAction("Custom Multi-Filters", self)
        multi_filter_action.triggered.connect(self.open_multi_filter_dialog)
        custom_menu.addAction(multi_filter_action)

    def change_filter_size(self):
        size = self.filter_size_combo.currentText()
        self.filter_size = int(size.split('x')[0])
        print(f"Selected filter size: {self.filter_size}x{self.filter_size}")

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            # Load ảnh với OpenCV
            self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            if self.image is None:
                QMessageBox.warning(self, "Error", "Failed to load image.")
                return
            # Hiển thị ảnh lên QLabel
            pixmap = self.array_to_pixmap(self.image)
            if pixmap:
                self.original_label.setPixmap(pixmap)
            else:
                QMessageBox.warning(self, "Error", "Failed to convert image for display.")

    def save_filtered_image(self):
        if self.filtered_label.pixmap() is None:
            QMessageBox.warning(self, "Error", "No filtered image to save!")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Filtered Image", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            pixmap = self.filtered_label.pixmap()
            pixmap.save(file_path)

    def apply_low_pass_filter(self):
        kernel = np.ones((self.filter_size, self.filter_size), np.float32) / (self.filter_size ** 2)
        self.apply_filter(kernel, "Low-Pass Filter Applied")

    def apply_high_pass_filter(self):
        size = self.filter_size
        kernel = -1 * np.ones((size, size), np.float32)
        kernel[size // 2, size // 2] = (size ** 2) - 1
        self.apply_filter(kernel, "High-Pass Filter Applied")

    def apply_derivative_filter(self):
        horizontal = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize=self.filter_size)
        vertical = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=self.filter_size)
        magnitude = np.sqrt(horizontal**2 + vertical**2)
        self.display_filtered_image(magnitude, "Sobel Filter Applied")

    def apply_median_filter(self):
        result = cv2.medianBlur(self.image, self.filter_size)
        self.display_filtered_image(result, "Median Filter Applied")

    def apply_min_filter(self):
        kernel = np.ones((self.filter_size, self.filter_size), np.uint8)
        result = cv2.erode(self.image, kernel)
        self.display_filtered_image(result, "Min Filter Applied")

    def apply_max_filter(self):
        kernel = np.ones((self.filter_size, self.filter_size), np.uint8)
        result = cv2.dilate(self.image, kernel)
        self.display_filtered_image(result, "Max Filter Applied")

    def apply_filter(self, kernel, message, return_image=False):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return

        gray_image = self.qimage_to_gray_array(self.image)
        filtered_array = cv2.filter2D(src=gray_image, ddepth=-1, kernel=kernel)

        if return_image:
            return filtered_array  # Return the filtered image if requested

        self.display_filtered_image(filtered_array, message)

    def apply_non_linear_filter(self, func, message):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return

        gray_image = self.qimage_to_gray_array(self.image)
        filtered_array = func(gray_image)
        self.display_filtered_image(filtered_array, message)

    def apply_median_filter(self):
        self.apply_non_linear_filter(
            lambda x: cv2.medianBlur(x, ksize=self.filter_size),
            "Median Filter Applied"
        )

    def apply_min_filter(self):
        self.apply_non_linear_filter(
            lambda x: cv2.erode(x, kernel=np.ones((self.filter_size, self.filter_size), np.uint8)),
            "Min Filter Applied"
        )

    def apply_max_filter(self):
        self.apply_non_linear_filter(
            lambda x: cv2.dilate(x, kernel=np.ones((self.filter_size, self.filter_size), np.uint8)),
            "Max Filter Applied"
        )

    def open_multi_filter_dialog(self):
        if self.image is None:
            QMessageBox.warning(self, "Error", "No image imported!")
            return

        dialog = MultiFilterDialog(self)
        dialog.exec_()

    def display_filtered_image(self, filtered_array, message):
        filtered_qimage = self.array_to_qimage(filtered_array)
        pixmap = QPixmap.fromImage(filtered_qimage)
        self.filtered_label.setPixmap(pixmap)
        self.bottom_widget.setText(message)

    def qimage_to_gray_array(self, image):
        ptr = image.bits()
        ptr.setsize(image.bytesPerLine() * image.height())
        arr = np.array(ptr).reshape((image.height(), image.bytesPerLine() // 4, 4))
        return cv2.cvtColor(arr[..., :3].astype(np.uint8), cv2.COLOR_RGB2GRAY)

    def array_to_qimage(self, array):
        array = np.clip(array, 0, 255).astype(np.uint8)
        height, width = array.shape
        return QImage(array.data, width, height, QImage.Format_Grayscale8)

    def array_to_pixmap(self, array):
        array = np.clip(array, 0, 255).astype(np.uint8)
        height, width = array.shape
        bytes_per_line = width
        q_image = QImage(array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap.fromImage(q_image)


def main():
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
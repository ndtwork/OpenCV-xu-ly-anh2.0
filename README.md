# Image Filtering Application

This project is a Python application that allows users to apply various filters to images using OpenCV and PyQt5 for the graphical user interface (GUI).

## Features

- Import and display images
- Apply different types of filters:
  - Low-pass filters
  - High-pass filters
  - Derivative filters
  - Median filters
  - Minimum filters
  - Maximum filters
  - Custom multi-filters
- Save filtered images

## Installation

### Prerequisites

- Python 3.12
- Miniconda or Anaconda
- numpy 1.26.4
- scipy 1.14.1
- opencv-python          4.10.0
- matplotlib             3.10.0
- PyQt5                  5.15.6


### Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate the conda environment:
    ```sh
    conda env create -f environment.yml -n <<tên môi trường >>
    conda activate <<tên môi trường>>
    ```
   then add conda enviroment to interpreter in Pycharm
Project > python interpreter > add > conda enviroment > existing enviroment > select enviroment

3. Install additional dependencies if needed:
use pip or conda to install directly

- numpy 1.26.4
- scipy 1.14.1
- opencv-python          4.10.0
- matplotlib             3.10.0
- PyQt5                  5.15.6

## Usage

1. Run the application:
    ```sh
    python ntdAPP2.py
    ```

2. Use the GUI to import an image, apply filters, and save the results.

## Project Structure

- `ntdAPP2.py`: is the lastest version to run the UI application
- `environment.yml`: Conda environment configuration file.
- `README.md`: Project documentation.
- `project` folder contain linear filter and nonlinear filter 

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

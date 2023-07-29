# Bing Watermark Remover

Welcome to Bing Watermark Remover, a GUI-based Python application that enables you to remove watermarks from images. This application has an easy-to-use graphical interface that helps in removing the watermarks from your images efficiently.

## Table of Contents

1. [About](#about)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technology Used](#technology-used)
5. [Contribution](#contribution)

## About

Bing Watermark Remover uses the Inpainting method, an image restoration process, to remove watermarks from images. This application works best with PNG files but can also process other image formats by first converting them to PNG.

## Installation

To install Bing Watermark Remover:

1. Ensure you have Python installed on your machine. If not, download and install Python from the official website (https://www.python.org/downloads/). This software was developed using Python 3.8 and might not work correctly with other versions.
   
2. Install the necessary Python libraries. You can do this by running the following command:

    ```
    pip install numpy pillow matplotlib opencv-python TKinterModernThemes 
    ```
   
3. Clone this repository to your local machine or download the Python script.

## Usage

1. Open the Python script using a Python interpreter.

2. Click the 'Run' button to start the program. You will be prompted to select the input files. 

3. Specify the output directory where the processed images should be saved. The program will begin processing the images immediately.

4. After all images have been processed, a completion window will pop up. You can choose to open the output folder or process another batch of images.

## Technology Used

Bing Watermark Remover uses the following Python libraries:

- **Tkinter**: Used for creating the GUI of the application.
- **TKinterModernThemes**: Used to apply modern themes to the GUI.
- **PIL (Pillow)**: Used for opening, manipulating, and saving different image file formats.
- **OpenCV**: Used for image processing tasks, particularly the inpainting method.
- **Numpy**: Used for handling arrays and performing mathematical operations.

## Contribution

We welcome contributions to this project! You can contribute in several ways:

1. Reporting Bugs: If you find any bugs or issues while using the software, please open an issue describing the problem.
2. Suggesting Enhancements: We would love to hear your ideas for new features or improvements! Please open an issue to share your suggestions.
3. Code Contributions: If you'd like to write code to fix bugs or add new features, please open a pull request. We would appreciate it if you first opened an issue describing what you intend to do.

We hope you find the Bing Watermark Remover useful, and we look forward to hearing your feedback!

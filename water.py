import os
from tkinter import Tk, filedialog
from PIL import Image
import cv2
import numpy as np

# Ask the user to select the files
root = Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames(title='Select files to process')

# Ask the user to specify the output directory
output_path = filedialog.askdirectory(title='Select output directory')

# Convert images to PNG format and apply the inpainting algorithm
for file_path in file_paths:
    if not file_path.lower().endswith('.png'):
        image = Image.open(file_path)
        output_file_path = os.path.join(output_path, os.path.splitext(os.path.basename(file_path))[0] + '.png')
        image.save(output_file_path)
    else:
        output_file_path = os.path.join(output_path, os.path.basename(file_path))

    img_cv = cv2.imread(file_path)
    height, width, _ = img_cv.shape
    mask = np.zeros((height, width), np.uint8)
    mask[int(0.95*height):, :int(0.05*width)] = 255
    result = cv2.inpaint(img_cv, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(output_file_path, result)

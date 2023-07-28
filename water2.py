import os
from tkinter import Tk, Label, Button, filedialog, Toplevel
from tkinter.ttk import Progressbar
import TKinterModernThemes as TKMT
from PIL import Image
import cv2
import numpy as np

def select_files():
    file_paths = filedialog.askopenfilenames(title='Select files to process')
    return file_paths

def select_output_dir():
    output_path = filedialog.askdirectory(title='Select output directory')
    return output_path

def process_files(file_paths, output_path, app):
    # Convert images to PNG format and apply the inpainting algorithm
    for i, file_path in enumerate(file_paths):
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

        # Update the progress bar
        app.progress_bar['value'] = (i + 1) / len(file_paths) * 100
        app.progress_label['text'] = f'Processing Files ({i + 1}/{len(file_paths)})'
        app.root.update_idletasks()

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("Bing Watermark Remover", "azure", "dark")
        
        label = Label(self.root, text='Bing Watermark Remover')
        label.pack(pady=10)

        description_label = Label(self.root, text='This program removes watermarks from images.\nClick the Run button to select the input files and specify the output directory.', justify='center', wraplength=350)
        description_label.pack(pady=10)

        run_button = Button(self.root, text='Run', command=self.on_run_button_click)
        run_button.pack(pady=10)

        self.progress_label = Label(self.root, text='')
        self.progress_label.pack(pady=10)

        self.progress_bar = Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

    def on_run_button_click(self):
        file_paths = select_files()
        output_path = select_output_dir()
        process_files(file_paths, output_path, self)

app = App()
app.run()

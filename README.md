# NmapToImagePager.py

NmapToImagePager is a Python script that reads `.nmap` files, paginates the content, and saves each page as a cropped image file. This tool is useful for visualizing large Nmap scan results, making them easier to review and share.

## Features

- Processes single `.nmap` files or all `.nmap` files in a specified directory.
- Paginates the content and saves each page as a cropped JPEG image.
- Automatically adjusts the number of lines per page to fill the image.
- Saves image files with leading zeros in filenames to ensure correct sorting.

## Requirements

- Python 3.x
- Pillow (PIL)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/NmapToImagePager.git
    cd NmapToImagePager
    ```

2. Install the required packages:
    ```bash
    pip install pillow
    ```

## Usage

To process a single `.nmap` file:
```bash
python NmapToImagePager.py <nmap_file>
```

To process a all `.nmap` files in a directory:
```bash
python NmapToImagePager.py <path to directory>
```

<br><br>   
# NmapImagesToWord.py

NmapImageToWord is a Python script that takes all images in a specified folder (typically created by `NmapToImagePager.py`), imports them into a Microsoft Word document, and arranges the images and captions within the document.

## Features

- Processes all images in a specified folder.
- Imports the images into a Word document.
- Centers images and captions, and styles captions in Calibri, 9 points.
- Captions each image with its filename.
- If no output filename is provided, the folder name will be used as the filename for the Word document.

## Requirements

- Python 3.x
- Pillow
- python-docx

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/NmapImageToWord.git
    cd NmapImageToWord
    ```

2. Install the required packages:
    ```bash
    pip install pillow python-docx
    ```

## Usage

To import all images from a folder into a Word document:
```bash
python NmapImagesToWord.py <image_folder> [output_filename]
```

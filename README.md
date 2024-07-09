# NmapToImagePager

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
python script.py <nmap_file>

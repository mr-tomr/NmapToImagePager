import os
import sys
from PIL import Image, ImageDraw, ImageFont

def calculate_lines_per_page(image_height, font_size):
    """
    Calculate the number of lines that fit in the given image height.
    """
    line_height = font_size + 5  # Adding some extra space for line spacing
    return image_height // line_height

def paginate(content, lines_per_page):
    """
    Generator that yields pages of content.
    """
    for i in range(0, len(content), lines_per_page):
        yield content[i:i + lines_per_page]

def save_page_to_image(page_content, folder, base_filename, page_number, image_width, image_height, font_size):
    """
    Save the page content to an image and crop the image around the text.
    """
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)

    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate line height
    line_height = font.getsize('A')[1]

    # Draw the text onto the image
    y = 10
    max_y = y
    for line in page_content:
        draw.text((10, y), line.strip(), fill=text_color, font=font)
        y += line_height
        max_y = y

    # Crop the image to fit the text
    cropped_image = image.crop((0, 0, image_width, max_y + 10))

    # Save the image with leading zeros in the file name
    filename = os.path.join(folder, f"{base_filename}_{page_number:03d}.jpg")
    cropped_image.save(filename)

def process_file(nmap_file):
    """
    Process a single nmap file.
    """
    if not os.path.isfile(nmap_file):
        print(f"Error: The file '{nmap_file}' does not exist.")
        return

    # Read the content of the nmap file
    with open(nmap_file, 'r') as file:
        content = file.readlines()

    # Create a folder named after the nmap file (without extension)
    base_filename = os.path.splitext(os.path.basename(nmap_file))[0]
    folder = base_filename
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Image settings
    image_width = 850
    image_height = 1100
    font_size = 15

    # Calculate lines per page based on the image height and font size
    lines_per_page = calculate_lines_per_page(image_height, font_size)

    # Paginate the content and save each page to an image
    for page_number, page_content in enumerate(paginate(content, lines_per_page), start=1):
        save_page_to_image(page_content, folder, base_filename, page_number, image_width, image_height, font_size)

    print(f"Pages saved to folder: {folder}")

def main(target):
    """
    Main function to process either a single nmap file or all nmap files in a directory.
    """
    if os.path.isfile(target):
        process_file(target)
    elif os.path.isdir(target):
        nmap_files = [f for f in os.listdir(target) if f.endswith('.nmap')]
        for nmap_file in nmap_files:
            process_file(os.path.join(target, nmap_file))
    else:
        print(f"Error: The target '{target}' is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <nmap_file_or_directory>")
        sys.exit(1)
    
    target = sys.argv[1]
    main(target)
